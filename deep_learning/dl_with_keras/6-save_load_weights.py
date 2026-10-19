#!/usr/bin/env python3
"""Introduction to Deep Learning with Keras Project
"""


def save_model_weights(model, filepath):
    """
    save
    """

    model.save_weights(filepath)


def load_model_weights(model, filepath):
    """
    load
    """
    model.load_weights(filepath)
