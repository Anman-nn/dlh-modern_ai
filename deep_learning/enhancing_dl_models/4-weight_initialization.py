#!/usr/bin/env python3
"""Enhancing Deep Learning Models
"""

from tensorflow import keras


def build_model_initializer_by_activation(
    input_dim,
    hidden_units,
    activation
):
    '''build_model_initializer_by_activation'''
    inputs = keras.Input(shape=(input_dim,))

    if activation in ("sigmoid", "tanh"):
        initializer = keras.initializers.GlorotUniform()
        hidden_activation = activation
    elif activation == "relu":
        initializer = keras.initializers.HeNormal()
        hidden_activation = "relu"
    elif activation == "leaky_relu":
        initializer = keras.initializers.HeNormal()
        hidden_activation = keras.layers.LeakyReLU()
    else:
        raise ValueError("Unsupported activation")

    hidden = keras.layers.Dense(
        hidden_units,
        activation=hidden_activation,
        kernel_initializer=initializer
    )(inputs)

    outputs = keras.layers.Dense(
        10,
        activation="softmax"
    )(hidden)

    model = keras.Model(inputs=inputs, outputs=outputs)

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model
