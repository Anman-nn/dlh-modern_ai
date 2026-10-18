#!/usr/bin/env python3
"""Introduction to Deep Learning with Keras Project
"""

from tensorflow import keras


def build_model(input_dim, neuros_h):
    model = keras.Sequential([
        keras.Input(shape=(input_dim,)),
        keras.layers.Dense(
            neuros_h,
            activation="sigmoid"
        ),
        keras.layers.Dense(
            10,
            activation="softmax"
        )
    ])

    return model
