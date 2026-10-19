#!/usr/bin/env python3
"""Introduction to Deep Learning with Keras Project
"""

from tensorflow import keras


def build_model(input_dim, neurons_h):
    '''build_model(input_dim, neurons_h)
    '''
    inputs = keras.Input(shape=(input_dim,))

    hidden = keras.layers.Dense(
        neurons_h,
        activation="sigmoid")(inputs)

    outputs = keras.layers.Dense(
        10,
        activation="softmax"
    )(hidden)

    model = keras.Model(
        inputs=inputs,
        outputs=outputs
    )

    return model
