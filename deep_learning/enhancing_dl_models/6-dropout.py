#!/usr/bin/env python3
"""Enhancing Deep Learning Models
"""

from tensorflow import keras


def build_model_with_dropout(
        input_dim, hidden_units,
        n_layers, dropout_rate_input,
        dropout_rate_hidden
        ):
    '''with dropout'''
    inputs = keras.layers.Input(shape=(input_dim,))
    x = keras.layers.Dropout(dropout_rate_input)(inputs)
    for units in range(0, n_layers):
        x = keras.layers.Dense(
            units=hidden_units,
            activation="relu"
            )(x)
        x = keras.layers.Dropout(dropout_rate_hidden)(x)

    outputs = keras.layers.Dense(units=10, activation="softmax")(x)

    model = keras.Model(inputs=inputs, outputs=outputs)

    return model
