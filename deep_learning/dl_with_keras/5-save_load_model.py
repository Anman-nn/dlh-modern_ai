#!/usr/bin/env python3
"""Introduction to Deep Learning with Keras Project
"""

from tensorflow import keras


def save_model(model, filepath):
    '''save
    '''
    model.save(filepath)


def load_model(filepath):
    '''load
    '''
    model = keras.models.load_model(filepath)
    return model
