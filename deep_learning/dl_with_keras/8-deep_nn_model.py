#!/usr/bin/env python3
"""Introduction to Deep Learning with Keras Project
"""

from tensorflow import keras


def build_deep_model(input_dim, hidden_layers):
    """
    build
    """
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(input_dim,)))

    for unit in hidden_layers:
        model.add(keras.layers.Dense(units=unit, activation="relu"))

    model.add(keras.layers.Dense(10, activation='softmax'))

    return model
