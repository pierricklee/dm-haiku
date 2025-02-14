# Copyright 2020 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
r"""Train a transformer for language modeling on a small text dataset.
This example serves to demonstrate:
  - A clean Haiku transformer implementation.
  - An example minimal training loop around it.
This example runs on ASCII text files.
We have not tuned the hyperparameters at all.
Example, using Karpathy's tiny_shakespeare dataset:
$ wget -O /tmp/shakespeare.txt \
    https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
$ python3 examples/transformer/train.py --dataset_path=/tmp/shakespeare.txt
Note: Run with --alsologtostderr to see outputs.
"""

from jaxlib import ipu_xla_client
import os 
cfg = ipu_xla_client.config.IPUConfig()
cfg.auto_select_ipus = 1
cfg.configure_ipu_system()
# input("pid: " + str(os.getpid()))
import functools
import os
import pickle
import time
from typing import Any, Mapping

from absl import app
from absl import flags
from absl import logging
import haiku as hk
import dataset
import model
import jax
import jax.numpy as jnp
import numpy as np
import optax

flags.DEFINE_string('dataset_path', None, 'Single-file ASCII dataset location.')

flags.DEFINE_integer('batch_size', 2, 'Train batch size per core')
flags.DEFINE_integer('sequence_length', 64, 'Sequence length to learn on')

flags.DEFINE_integer('d_model', 128, 'model width')
flags.DEFINE_integer('num_heads', 4, 'Number of attention heads')
flags.DEFINE_integer('num_layers', 4, 'Number of transformer layers')
flags.DEFINE_float('dropout_rate', 0.1, 'Dropout rate')

flags.DEFINE_float('learning_rate', 3e-4, 'Max learning-rate')
flags.DEFINE_float('grad_clip_value', 1, 'Gradient norm clip value')

flags.DEFINE_string('checkpoint_dir', '/tmp/haiku-transformer',
                    'Directory to store checkpoints.')

FLAGS = flags.FLAGS
LOG_EVERY = 50
# MAX_STEPS = 10**6
MAX_STEPS = 1000



def build_forward_fn(vocab_size: int, d_model: int, num_heads: int,
                     num_layers: int, dropout_rate: float):
  """Create the model's forward pass."""

  def forward_fn(data: Mapping[str, jnp.ndarray],
                 is_training: bool = True) -> jnp.ndarray:
    """Forward pass."""
    tokens = data['obs']
    input_mask = jnp.greater(tokens, 0)
    seq_length = tokens.shape[1]

    # Embed the input tokens and positions.
    embed_init = hk.initializers.TruncatedNormal(stddev=0.02)
    token_embedding_map = hk.Embed(vocab_size, d_model, w_init=embed_init)
    token_embs = token_embedding_map(tokens)
    positional_embeddings = hk.get_parameter(
        'pos_embs', [seq_length, d_model], init=embed_init)
    input_embeddings = token_embs + positional_embeddings

    # Run the transformer over the inputs.
    transformer = model.Transformer(
        num_heads=num_heads, num_layers=num_layers, dropout_rate=dropout_rate)
    output_embeddings = transformer(input_embeddings, input_mask, is_training)

    # Reverse the embeddings (untied).
    return hk.Linear(vocab_size)(output_embeddings)

  return forward_fn


def lm_loss_fn(forward_fn,
               vocab_size: int,
               params,
               rng,
               data: Mapping[str, jnp.ndarray],
               is_training: bool = True) -> jnp.ndarray:
  """Compute the loss on data wrt params."""
  logits = forward_fn(params, rng, data, is_training)
  targets = jax.nn.one_hot(data['target'], vocab_size)
  assert logits.shape == targets.shape

  mask = jnp.greater(data['obs'], 0)
  loss = -jnp.sum(targets * jax.nn.log_softmax(logits), axis=-1)
  loss = jnp.sum(loss * mask) / jnp.sum(mask)

  return loss


class Updater:
  """A stateless abstraction around an init_fn/update_fn pair.
  This extracts some common boilerplate from the training loop.
  """

  def __init__(self, net_init, loss_fn,
               optimizer: optax.GradientTransformation):
    self._net_init = net_init
    self._loss_fn = loss_fn
    self._opt = optimizer

  @functools.partial(jax.jit, static_argnums=0)
  def init(self, rng, data):
    """Initializes state of the updater."""
    out_rng, init_rng = jax.random.split(rng)
    params = self._net_init(init_rng, data)
    opt_state = self._opt.init(params)
    out = dict(
        step=np.array(0),
        rng=out_rng,
        opt_state=opt_state,
        params=params,
    )
    return out

  @functools.partial(jax.jit, static_argnums=0)
  def update(self, state: Mapping[str, Any], data: Mapping[str, jnp.ndarray]):
    """Updates the state using some data and returns metrics."""
    rng, new_rng = jax.random.split(state['rng'])
    params = state['params']
    loss, g = jax.value_and_grad(self._loss_fn)(params, rng, data)

    updates, opt_state = self._opt.update(g, state['opt_state'])
    params = optax.apply_updates(params, updates)

    new_state = {
        'step': state['step'] + 1,
        'rng': new_rng,
        'opt_state': opt_state,
        'params': params,
    }

    metrics = {
        'step': state['step'],
        'loss': loss,
    }
    return new_state, metrics


class CheckpointingUpdater:
  """A didactic checkpointing wrapper around an Updater.
  A more mature checkpointing implementation might:
    - Use np.savez() to store the core data instead of pickle.
    - Not block JAX async dispatch.
    - Automatically garbage collect old checkpoints.
  """

  def __init__(self,
               inner: Updater,
               checkpoint_dir: str,
               checkpoint_every_n: int = 10000):
    self._inner = inner
    self._checkpoint_dir = checkpoint_dir
    self._checkpoint_every_n = checkpoint_every_n

  def _checkpoint_paths(self):
    return [p for p in os.listdir(self._checkpoint_dir) if 'checkpoint_' in p]

  def init(self, rng, data):
    """Initialize experiment state."""
    if not os.path.exists(self._checkpoint_dir) or not self._checkpoint_paths():
      os.makedirs(self._checkpoint_dir, exist_ok=True)
      return self._inner.init(rng, data)
    else:
      checkpoint = os.path.join(self._checkpoint_dir,
                                max(self._checkpoint_paths()))
      logging.info('Loading checkpoint from %s', checkpoint)
      with open(checkpoint, 'rb') as f:
        state = pickle.load(f)
      return state

  def update(self, state, data):
    """Update experiment state."""
    # NOTE: This blocks until `state` is computed. If you want to use JAX async
    # dispatch, maintain state['step'] as a NumPy scalar instead of a JAX array.
    # Context: https://jax.readthedocs.io/en/latest/async_dispatch.html
    step = np.array(state['step'])
    if step % self._checkpoint_every_n == 0:
      path = os.path.join(self._checkpoint_dir,
                          'checkpoint_{:07d}.pkl'.format(step))
      checkpoint_state = jax.device_get(state)
      logging.info('Serializing experiment state to %s', path)
      with open(path, 'wb') as f:
        pickle.dump(checkpoint_state, f)

    state, out = self._inner.update(state, data)
    return state, out


def main(_):
  FLAGS.alsologtostderr = True  # Always log visibly.
  # Create the dataset.
  train_dataset = dataset.AsciiDataset(
      FLAGS.dataset_path, FLAGS.batch_size, FLAGS.sequence_length)
  vocab_size = train_dataset.vocab_size

  # Set up the model, loss, and updater.
  print("Before forward_fn")
  forward_fn = build_forward_fn(vocab_size, FLAGS.d_model, FLAGS.num_heads,
                                FLAGS.num_layers, FLAGS.dropout_rate)
  forward_fn = hk.transform(forward_fn)
  loss_fn = functools.partial(lm_loss_fn, forward_fn.apply, vocab_size)

  print("Before optimizer optax.chain")
  optimizer = optax.chain(
      optax.clip_by_global_norm(FLAGS.grad_clip_value),
      optax.adam(FLAGS.learning_rate, b1=0.9, b2=0.99))

  print("Before updater, Updater, CheckpointingUpdater")
  updater = Updater(forward_fn.init, loss_fn, optimizer)
  updater = CheckpointingUpdater(updater, FLAGS.checkpoint_dir)

  # Initialize parameters.
  logging.info('Initializing parameters...')
  rng = jax.random.PRNGKey(428)
  data = next(train_dataset)
  state = updater.init(rng, data)

  logging.info('Starting train loop...')
#   input("pid: " + str(os.getpid()))
  prev_time = time.time()
  for step in range(MAX_STEPS):
    data = next(train_dataset)
    state, metrics = updater.update(state, data)
    # We use JAX runahead to mask data preprocessing and JAX dispatch overheads.
    # Using values from state/metrics too often will block the runahead and can
    # cause these overheads to become more prominent.
    if step % LOG_EVERY == 0:
      steps_per_sec = LOG_EVERY / (time.time() - prev_time)
      prev_time = time.time()
      metrics.update({'steps_per_sec': steps_per_sec})
      logging.info({k: float(v) for k, v in metrics.items()})


if __name__ == '__main__':
  flags.mark_flag_as_required('dataset_path')
  app.run(main)