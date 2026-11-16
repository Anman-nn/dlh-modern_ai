#!/usr/bin/env python3
"""Computer Vision Architectures
"""

from tensorflow import keras as K


def depthwise_separable_conv(X, filters, stride=1):
    '''depthwise_separable_conv()'''
    x = K.layers.DepthwiseConv2D(
        kernel_size=(3, 3), strides=stride,
        padding='same', use_bias=False
    )(X)
    x = K.layers.BatchNormalization()(x)
    x = K.layers.ReLU()(x)

    x = K.layers.Conv2D(
        filters=filters, kernel_size=(1, 1),
        strides=1, padding='same',
        use_bias=False
    )(x)
    x = K.layers.BatchNormalization()(x)
    x = K.layers.ReLU()(x)

    return x
