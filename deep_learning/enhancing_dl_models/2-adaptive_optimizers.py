#!/usr/bin/env python3
"""Enhancing Deep Learning Models
"""

from tensorflow import keras


def get_optimizer(name, learning_rate, momentum, beta_1, beta_2, rho):
    '''get_optimizer'''
    if name == "sgd":
        optimizer = keras.optimizers.SGD(
            learning_rate=learning_rate,
            momentum=momentum
        )
    elif name == "adam":
        optimizer = keras.optimizers.Adam(
            learning_rate=learning_rate,
            beta_1=beta_1,
            beta_2=beta_2,
            ema_momentum=momentum
        )
    elif name == "rmsprop":
        optimizer = keras.optimizers.RMSprop(
            learning_rate=learning_rate,
            momentum=momentum,
            rho=rho
        )
    else:
        raise ValueError(
            "variant must be 'batch', 'stochastic', or 'mini_batch'"
        )

    return optimizer
