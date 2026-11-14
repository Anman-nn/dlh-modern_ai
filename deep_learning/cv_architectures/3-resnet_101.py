#!/usr/bin/env python3
"""Computer Vision Architectures
"""

from tensorflow import keras
bottleneck_block = __import__('2-bottleneck_block').bottleneck_block


def make_layer(x, blocks, filters, stride=1, name=None):
    '''def make_layer'''
    x = bottleneck_block(x, filters, stride=stride, downsample=True,
                         name=f'{name}_block1')
    for i in range(1, blocks):
        x = bottleneck_block(x, filters, stride=1, downsample=False,
                             name=f'{name}_block{i+1}')
    return x


def build_resnet101(input_shape=(224, 224, 3), num_classes=1000):
    '''build_resnet101'''
    inputs = keras.Input(shape=input_shape)

    x = keras.layers.Conv2D(
        64, 7, strides=2, padding='same', use_bias=False,
        name='conv1')(inputs)
    x = keras.layers.BatchNormalization(name='bn1')(x)
    x = keras.layers.ReLU(name='relu1')(x)
    x = keras.layers.MaxPooling2D(
        3, strides=2, padding='same', name='maxpool')(x)

    x = make_layer(x, blocks=3, filters=64, stride=1, name='conv2')
    x = make_layer(x, blocks=4, filters=128, stride=2, name='conv3')
    x = make_layer(x, blocks=23, filters=256, stride=2, name='conv4')
    x = make_layer(x, blocks=3, filters=512, stride=2, name='conv5')

    x = keras.layers.GlobalAveragePooling2D(name='avgpool')(x)
    outputs = keras.layers.Dense(
        num_classes, activation='softmax', name='fc')(x)

    model = keras.Model(inputs=inputs, outputs=outputs, name='resnet101')

    return model
