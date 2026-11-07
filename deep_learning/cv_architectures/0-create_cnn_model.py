#!/usr/bin/env python3
"""Computer Vision Architectures
"""

import keras
from keras import layers


def create_cnn_model(input_shape, filters, kernel_sizes,
    activations, pooling_type='max'):
    '''create CNN model'''

    ki = keras.Input(shape=input_shape)

    l1_c2d = layers.Conv2D(
        filters=filters[0],
        kernel_size=kernel_sizes[0],
        activation=activations[0],
        padding="same"
    )
    if pooling_type == "max":
        pooling_class = layers.MaxPooling2D
    elif pooling_type == "avg":
        pooling_class = layers.AveragePooling2D

    l_pooling1 = pooling_class(pool_size=(2, 2))
    l_pooling2 = pooling_class(pool_size=(2, 2))

    l2_c2d = layers.Conv2D(
        filters=filters[1],
        kernel_size=kernel_sizes[1],
        activation=activations[1],
        padding="same"
    )
    l_f = layers.Flatten()
    l_d = layers.Dense(units=10, activation='softmax')

    model = keras.Sequential([ki, l1_c2d, l_pooling1,
                              l2_c2d, l_pooling2, l_f, l_d]
    )

    return model
