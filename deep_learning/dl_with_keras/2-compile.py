#!/usr/bin/env python3
"""Introduction to Deep Learning with Keras Project
"""

from tensorflow import keras


def compile_model(model, learning_rate=0.01):
    '''compile'''
    model.compile(
        optimizer=keras.optimizers.SGD(learning_rate=learning_rate),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
