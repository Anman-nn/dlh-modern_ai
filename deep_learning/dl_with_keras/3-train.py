#!/usr/bin/env python3
"""Introduction to Deep Learning with Keras Project
"""

from tensorflow import keras


def train_model(model, X, Y, epochs, verbose=1):
    '''train_model(model, X, Y, epochs, verbose=1)'''
    model.fit(
        X,
        Y,
        epochs=epochs,
        verbose=verbose
    )
