#!/usr/bin/env python3
"""Enhancing Deep Learning Models
"""

from tensorflow import keras


def train_with_gradient_descent_variant(variant, learning_rate, x_train, batch_size):
    '''train_with_gradient_descent_variant'''
    optimizer = keras.optimizers.SGD(
        learning_rate=learning_rate
    )

    if variant == "batch":
        bs = len(x_train)
    elif variant == "stochastic":
        bs = 1
    elif variant == "mini_batch":
        bs = batch_size
    else:
        raise ValueError(
            "variant must be 'batch', 'stochastic', or 'mini_batch'"
        )

    return optimizer, bs
