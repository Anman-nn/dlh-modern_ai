#!/usr/bin/env python3
"""Introduction to Deep Learning with Keras Project
"""


import tensorflow as tf


def predict(model, X, verbose=0):
    """
    predict
    """
    probabilities = model.predict(X, verbose=verbose)
    prediction = tf.argmax(probabilities, axis=1)

    return prediction
