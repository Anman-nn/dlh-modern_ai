#!/usr/bin/env python3
"""Computer Vision Architectures
"""

from tensorflow import keras


def create_cnn_model(
    input_shape,
    filters,
    kernel_sizes,
    activations,
    pooling_type="max"
):
    """Create CNN model."""

    if pooling_type == "max":
        pooling_class = keras.layers.MaxPooling2D
    elif pooling_type == "avg":
        pooling_class = keras.layers.AveragePooling2D
    else:
        raise ValueError(
            "pooling_type must be 'max' or 'average'"
        )

    model = keras.Sequential([
        keras.Input(shape=input_shape),

        keras.layers.Conv2D(
            filters=filters[0],
            kernel_size=kernel_sizes[0],
            activation=activations[0]
        ),
        pooling_class(pool_size=(2, 2)),

        keras.layers.Conv2D(
            filters=filters[1],
            kernel_size=kernel_sizes[1],
            activation=activations[1]
        ),
        pooling_class(pool_size=(2, 2)),

        keras.layers.Flatten(),

        keras.layers.Dense(
            units=10,
            activation="softmax"
        )
    ])

    return model
