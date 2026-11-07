#!/usr/bin/env python3
"""Computer Vision Architectures
"""

from tensorflow import keras


def create_cnn_model(input_shape, filters, kernel_sizes,
    activations, pooling_type='max'):
    '''create CNN model'''

    ki = keras.Input(shape=input_shape)

    l1_c2d = keras.layers.Conv2D(
        filters=filters[0],
        kernel_size=kernel_sizes[0],
        activation=activations[0],
        padding="same"
    )
    if pooling_type == "max":
        pooling_class = keras.layers.MaxPooling2D
    elif pooling_type == "avg":
        pooling_class = keras.layers.AveragePooling2D

    l_pooling1 = pooling_class(pool_size=(2, 2))
    l_pooling2 = pooling_class(pool_size=(2, 2))

    l2_c2d = keras.layers.Conv2D(
        filters=filters[1],
        kernel_size=kernel_sizes[1],
        activation=activations[1],
        padding="same"
    )
    l_f = keras.layers.Flatten()
    l_d = keras.layers.Dense(units=10, activation='softmax')

    model = keras.Sequential([ki, l1_c2d, l_pooling1,
                              l2_c2d, l_pooling2, l_f, l_d]
    )

    return model
