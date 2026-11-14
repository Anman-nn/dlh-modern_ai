#!/usr/bin/env python3
"""Computer Vision Architectures
"""

from tensorflow import keras


def bottleneck_block(
    x, filters, stride=1, downsample=False, name=None
):
    '''bottleneck_block'''
    bn = x

    bn = keras.layers.Conv2D(
        filters=filters,
        kernel_size=(1, 1),
        strides=stride,
        use_bias=False,
        name=f"{name}_conv1" if name else None
        )(bn)
    bn = keras.layers.BatchNormalization(
        name=f"{name}_bn1" if name else None
        )(bn)
    bn = keras.layers.Activation(
        'relu',
        name=f"{name}_relu1" if name else None
        )(bn)

    # 3x3
    bn = keras.layers.Conv2D(
        filters=filters,
        kernel_size=(3, 3),
        padding='same',
        use_bias=False,
        name=f"{name}_conv2" if name else None
        )(bn)
    bn = keras.layers.BatchNormalization(
        name=f"{name}_bn2" if name else None
        )(bn)
    bn = keras.layers.Activation(
        'relu',
        name=f"{name}_relu2" if name else None
        )(bn)

    # 1x1
    bn = keras.layers.Conv2D(
        filters=filters * 4,
        kernel_size=(1, 1),
        use_bias=False,
        name=f"{name}_conv3" if name else None
        )(bn)
    bn = keras.layers.BatchNormalization(
        name=f"{name}_bn3" if name else None
        )(bn)

    # shortcut
    if downsample:
        sc = keras.layers.Conv2D(
            filters=filters * 4,
            kernel_size=(1, 1),
            strides=stride,
            use_bias=False,
            name=f"{name}_shortcut_conv" if name else None
            )(x)

        sc = keras.layers.BatchNormalization(
            name=f"{name}_shortcut_bn" if name else None
            )(sc)

    else:
        sc = x

    out = keras.layers.add(
        [bn, sc],
        name=f"{name}_add" if name else None
        )
    out = keras.layers.Activation(
        'relu',
        name=f"{name}_out" if name else None
        )(out)

    return out