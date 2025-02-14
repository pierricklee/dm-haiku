Haiku Fundamentals
==================

.. currentmodule:: haiku

Haiku Transforms
----------------

.. autosummary::

    transform
    transform_with_state
    without_apply_rng
    without_state

transform
~~~~~~~~~

.. autofunction:: transform

transform_with_state
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: transform_with_state

without_apply_rng
~~~~~~~~~~~~~~~~~

.. autofunction:: without_apply_rng

without_state
~~~~~~~~~~~~~

.. autofunction:: without_state

Modules, Parameters and State
-----------------------------

.. autosummary::

    Module
    to_module
    get_parameter
    get_state
    set_state
    transparent

Module
~~~~~~

.. autoclass:: Module
   :members:

to_module
~~~~~~~~~

.. autofunction:: to_module

get_parameter
~~~~~~~~~~~~~

.. autofunction:: get_parameter

get_state
~~~~~~~~~

.. autofunction:: get_state

set_state
~~~~~~~~~

.. autofunction:: set_state

transparent
~~~~~~~~~~~~

.. autofunction:: transparent

Random Numbers
--------------

.. autosummary::

    PRNGSequence
    next_rng_key
    next_rng_keys
    maybe_next_rng_key
    reserve_rng_keys
    with_rng

PRNGSequence
~~~~~~~~~~~~

.. autoclass:: PRNGSequence
   :members:

next_rng_key
~~~~~~~~~~~~

.. autofunction:: next_rng_key

next_rng_keys
~~~~~~~~~~~~~

.. autofunction:: next_rng_keys

maybe_next_rng_key
~~~~~~~~~~~~~~~~~~

.. autofunction:: maybe_next_rng_key

reserve_rng_keys
~~~~~~~~~~~~~~~~

.. autofunction:: reserve_rng_keys

with_rng
~~~~~~~~

.. autofunction:: with_rng

Type Hints
----------

.. autosummary::

    LSTMState
    Params
    State
    Transformed
    TransformedWithState

LSTMState
~~~~~~~~~

.. autoclass:: LSTMState

Params
~~~~~~

.. autoclass:: Params

State
~~~~~

.. autoclass:: State

Transformed
~~~~~~~~~~~

.. autoclass:: Transformed

TransformedWithState
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: TransformedWithState

Common Modules
==============

Linear
------

.. autosummary::

    Linear
    Bias

Linear
~~~~~~

.. autoclass:: Linear
   :members:

Bias
~~~~

.. autoclass:: Bias
   :members:

Pooling
-------

.. currentmodule:: haiku

.. autosummary::

    avg_pool
    AvgPool
    max_pool
    MaxPool

Average Pool
~~~~~~~~~~~~

.. autofunction:: avg_pool

.. autoclass:: AvgPool
   :members:

Max Pool
~~~~~~~~

.. autofunction:: max_pool

.. autoclass:: MaxPool
   :members:

Dropout
-------

.. autosummary::

    dropout

dropout
~~~~~~~

.. autofunction:: dropout

Combinator
----------

.. autosummary::

    Sequential

Sequential
~~~~~~~~~~

.. autoclass:: Sequential
  :members:

Convolutional
-------------

.. currentmodule:: haiku

.. autosummary::

    ConvND
    Conv1D
    Conv2D
    Conv3D
    ConvNDTranspose
    Conv1DTranspose
    Conv2DTranspose
    Conv3DTranspose
    DepthwiseConv2D
    DepthwiseConv2D

ConvND
~~~~~~

.. autoclass:: ConvND
   :members:

Conv1D
~~~~~~

.. autoclass:: Conv1D
   :members:

Conv2D
~~~~~~

.. autoclass:: Conv2D
   :members:

Conv3D
~~~~~~

.. autoclass:: Conv3D
   :members:

ConvNDTranspose
~~~~~~~~~~~~~~~

.. autoclass:: ConvNDTranspose
   :members:

Conv1DTranspose
~~~~~~~~~~~~~~~

.. autoclass:: Conv1DTranspose
   :members:

Conv2DTranspose
~~~~~~~~~~~~~~~

.. autoclass:: Conv2DTranspose
   :members:

Conv3DTranspose
~~~~~~~~~~~~~~~

.. autoclass:: Conv3DTranspose
   :members:

DepthwiseConv2D
~~~~~~~~~~~~~~~

.. autoclass:: DepthwiseConv2D
   :members:


SeparableDepthwiseConv2D
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: DepthwiseConv2D
   :members:

Normalization
-------------

.. currentmodule:: haiku

.. autosummary::

    BatchNorm
    GroupNorm
    InstanceNorm
    LayerNorm
    SpectralNorm
    ExponentialMovingAverage
    SNParamsTree
    EMAParamsTree

BatchNorm
~~~~~~~~~

.. autoclass:: BatchNorm
   :members:

GroupNorm
~~~~~~~~~

.. autoclass:: GroupNorm
   :members:

InstanceNorm
~~~~~~~~~~~~

.. autoclass:: InstanceNorm
   :members:

LayerNorm
~~~~~~~~~

.. autoclass:: LayerNorm
   :members:

SpectralNorm
~~~~~~~~~~~~

.. autoclass:: SpectralNorm
   :members:

ExponentialMovingAverage
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: ExponentialMovingAverage
   :members:

SNParamsTree
~~~~~~~~~~~~

.. autoclass:: SNParamsTree
   :members:

EMAParamsTree
~~~~~~~~~~~~~

.. autoclass:: EMAParamsTree
   :members:

Recurrent
---------

.. currentmodule:: haiku

.. autosummary::

    RNNCore
    dynamic_unroll
    static_unroll
    expand_apply
    VanillaRNN
    LSTM
    GRU
    DeepRNN
    deep_rnn_with_skip_connections
    ResetCore
    IdentityCore
    Conv1DLSTM
    Conv2DLSTM
    Conv3DLSTM

RNNCore
~~~~~~~

.. autoclass:: RNNCore
   :members:

dynamic_unroll
~~~~~~~~~~~~~~

.. autofunction:: dynamic_unroll

static_unroll
~~~~~~~~~~~~~~

.. autofunction:: static_unroll

expand_apply
~~~~~~~~~~~~

.. autofunction:: expand_apply

VanillaRNN
~~~~~~~~~~

.. autoclass:: VanillaRNN
   :members:
   :special-members:

LSTM
~~~~

.. autoclass:: LSTM
   :members:

GRU
~~~

.. autoclass:: GRU
   :members:

DeepRNN
~~~~~~~

.. autoclass:: DeepRNN
   :members:

.. autofunction:: deep_rnn_with_skip_connections

ResetCore
~~~~~~~~~

.. autoclass:: ResetCore
   :members:

IdentityCore
~~~~~~~~~~~~

.. autoclass:: IdentityCore
   :members:

Conv1DLSTM
~~~~~~~~~~~~~~~

.. autoclass:: Conv1DLSTM
   :members:

Conv2DLSTM
~~~~~~~~~~~~~~~

.. autoclass:: Conv2DLSTM
   :members:

Conv3DLSTM
~~~~~~~~~~~~~~~

.. autoclass:: Conv3DLSTM
   :members:

Attention
-----------------

.. currentmodule:: haiku

MultiHeadAttention
~~~~~~~~~~~~~~~~~~

.. autoclass:: MultiHeadAttention
   :members:

Batch
-----

.. currentmodule:: haiku

.. autosummary::

    Reshape
    Flatten
    BatchApply

Reshape
~~~~~~~

.. autoclass:: Reshape
   :members:

Flatten
~~~~~~~

.. autoclass:: Flatten
   :members:

BatchApply
~~~~~~~~~~

.. autoclass:: BatchApply
   :members:

Embedding
---------

.. currentmodule:: haiku

.. autosummary::

    Embed
    EmbedLookupStyle

Embed
~~~~~

.. autoclass:: Embed
   :members:

EmbedLookupStyle
~~~~~~~~~~~~~~~~

.. autoclass:: EmbedLookupStyle
   :members:

Initializers
------------

.. automodule:: haiku.initializers

.. autosummary::

    Initializer
    Constant
    Identity
    Orthogonal
    RandomNormal
    RandomUniform
    TruncatedNormal
    VarianceScaling
    UniformScaling

Initializer
~~~~~~~~~~~

.. autoclass:: Initializer
   :members:

Constant
~~~~~~~~

.. autoclass:: Constant
   :members:

Identity
~~~~~~~~

.. autoclass:: Identity
   :members:

Orthogonal
~~~~~~~~~~

.. autoclass:: Orthogonal
   :members:

RandomNormal
~~~~~~~~~~~~

.. autoclass:: RandomNormal
   :members:

RandomUniform
~~~~~~~~~~~~~

.. autoclass:: RandomUniform
   :members:

TruncatedNormal
~~~~~~~~~~~~~~~

.. autoclass:: TruncatedNormal
   :members:

VarianceScaling
~~~~~~~~~~~~~~~

.. autoclass:: VarianceScaling
   :members:

UniformScaling
~~~~~~~~~~~~~~

.. autoclass:: UniformScaling
   :members:

Paddings
--------

.. automodule:: haiku.pad

.. autosummary::

    PadFn
    create
    causal
    full
    reverse_causal
    same
    valid

PadFn
~~~~~

.. autoclass:: PadFn
   :members:

create
~~~~~~

.. autofunction:: create

causal
~~~~~~

.. autofunction:: causal

full
~~~~

.. autofunction:: full

reverse_causal
~~~~~~~~~~~~~~

.. autofunction:: reverse_causal

same
~~~~

.. autofunction:: same

valid
~~~~~

.. autofunction:: valid

Full Networks
=============

.. automodule:: haiku.nets

MLP
---

.. autoclass:: MLP
   :members:

MobileNet
---------

MobileNetV1
~~~~~~~~~~~

.. autoclass:: MobileNetV1
   :members:

ResNet
------

.. autosummary::

    ResNet
    ResNet.BlockGroup
    ResNet.BlockV1
    ResNet.BlockV2
    ResNet18
    ResNet34
    ResNet50
    ResNet101
    ResNet152
    ResNet200

ResNet
~~~~~~

.. autoclass:: ResNet
   :members:

ResNet18
~~~~~~~~

.. autoclass:: ResNet18
   :members:

ResNet34
~~~~~~~~

.. autoclass:: ResNet34
   :members:

ResNet50
~~~~~~~~

.. autoclass:: ResNet50
   :members:

ResNet101
~~~~~~~~~

.. autoclass:: ResNet101
   :members:

ResNet152
~~~~~~~~~

.. autoclass:: ResNet152
   :members:

ResNet200
~~~~~~~~~

.. autoclass:: ResNet200
   :members:

VectorQuantizer
---------------

.. autosummary::

    VectorQuantizer
    VectorQuantizerEMA

VectorQuantizer
~~~~~~~~~~~~~~~

.. autoclass:: VectorQuantizer
   :members:

VectorQuantizerEMA
~~~~~~~~~~~~~~~~~~

.. autoclass:: VectorQuantizerEMA
   :members:

JAX Fundamentals
================

.. currentmodule:: haiku

Control Flow
------------

.. autosummary::

    cond
    fori_loop
    scan
    switch
    while_loop

cond
~~~~

.. autofunction:: cond

fori_loop
~~~~~~~~~

.. autofunction:: fori_loop

scan
~~~~

.. autofunction:: scan

switch
~~~~~~

.. autofunction:: switch

while_loop
~~~~~~~~~~

.. autofunction:: while_loop

JAX Transforms
--------------

.. autosummary::

    grad
    jit
    remat
    value_and_grad
    vmap

grad
~~~~

.. autofunction:: grad

jit
~~~

.. autofunction:: jit

remat
~~~~~

.. autofunction:: remat

value_and_grad
~~~~~~~~~~~~~~

.. autofunction:: value_and_grad

vmap
~~~~

.. autofunction:: vmap

🚧 Experimental
===============

.. automodule:: haiku.experimental

.. autosummary::

    abstract_to_dot
    custom_creator
    custom_getter
    GetterContext
    intercept_methods
    MethodContext
    name_scope
    named_call
    optimize_rng_use
    lift
    profiler_name_scopes
    to_dot


abstract_to_dot
------

.. autofunction:: abstract_to_dot

custom_creator
--------------

.. autofunction:: custom_creator

custom_getter
-------------

.. autofunction:: custom_getter

GetterContext
-------------

.. autoclass:: GetterContext

ParamContext
------------

.. deprecated:: 0.0.3
  Renamed to :class:`GetterContext` and used for both custom parameter getters
  and custom state getters.

.. autoclass:: ParamContext

intercept_methods
-----------------

.. autofunction:: intercept_methods

MethodContext
-------------

.. autoclass:: MethodContext

name_scope
----------

.. autofunction:: name_scope

named_call
----------

.. autofunction:: named_call

optimize_rng_use
----------------

.. autofunction:: optimize_rng_use

lift
----

.. autofunction:: lift

profiler_name_scopes
--------------------

.. autofunction:: profiler_name_scopes

to_dot
------

.. autofunction:: to_dot

Utilities
=========

.. currentmodule:: haiku

Data Structures
---------------

.. automodule:: haiku.data_structures

.. autosummary::

    filter
    merge
    partition
    to_immutable_dict
    to_mutable_dict
    tree_bytes
    tree_size

filter
~~~~~~

.. autofunction:: filter

merge
~~~~~

.. autofunction:: merge

partition
~~~~~~~~~

.. autofunction:: partition

to_immutable_dict
~~~~~~~~~~~~~~~~~

.. autofunction:: to_immutable_dict

to_mutable_dict
~~~~~~~~~~~~~~~

.. autofunction:: to_mutable_dict

tree_bytes
~~~~~~~~~~

.. autofunction:: tree_bytes

tree_size
~~~~~~~~~

.. autofunction:: tree_size

Testing
-------

.. automodule:: haiku.testing

.. autosummary::

    transform_and_run

transform_and_run
~~~~~~~~~~~~~~~~~

.. autofunction:: transform_and_run

Conditional Computation
-----------------------

.. automodule:: haiku

.. autosummary::

    running_init

running_init
~~~~~~~~~~~~

.. autofunction:: running_init

Functions
---------

.. automodule:: haiku

.. autosummary::

    multinomial
    one_hot

multinomial
~~~~~~~~~~~

.. autofunction:: multinomial

one_hot
~~~~~~~

.. autofunction:: one_hot

References
==========

.. bibliography:: references.bib
   :style: unsrt
