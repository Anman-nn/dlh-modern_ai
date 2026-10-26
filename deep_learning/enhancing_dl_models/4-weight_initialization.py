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
        hidden = keras.layers.Dense(
            hidden_units,
            activation=activation,
            kernel_initializer=keras.initializers.GlorotUniform()
        )(inputs)

    elif activation == "relu":
        hidden = keras.layers.Dense(
            hidden_units,
            activation="relu",
            kernel_initializer=keras.initializers.HeNormal()
        )(inputs)

    elif activation == "leaky_relu":
        hidden = keras.layers.Dense(
            hidden_units,
            kernel_initializer=keras.initializers.HeNormal()
        )(inputs)

        hidden = keras.layers.LeakyReLU()(hidden)

    else:
        raise ValueError(
            "activation must be 'sigmoid', 'tanh', "
            "'relu', or 'leaky_relu'"
        )

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
