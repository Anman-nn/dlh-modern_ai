#!/usr/bin/env python3
"""Enhancing Deep Learning Models
"""

from tensorflow import keras


def get_optimizer_SGD(name, lr, momentum=0.0, nesterov=False):
    '''get_optimizer_SGD(name, lr, momentum=0.0, nesterov=False)'''

    if name == "SGD":
        optimizer = keras.optimizers.SGD(
            learning_rate=lr
        )
    elif name == "SGD+Momentum":
        optimizer = keras.optimizers.SGD(
            learning_rate=lr,
            momentum=momentum
        )
    elif name == "SGD+Momentum+Nesterov":
        optimizer = keras.optimizers.SGD(
            learning_rate=lr,
            momentum=momentum,
            nesterov=nesterov
        )
    else:
        raise ValueError(
            "variant must be 'batch', 'stochastic', or 'mini_batch'"
        )

    return optimizer
