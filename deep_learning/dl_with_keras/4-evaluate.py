#!/usr/bin/env python3
"""Introduction to Deep Learning with Keras Project
"""


def evaluate_model(model, X, Y, verbose=0):
    '''evaluate_model(model, X, Y, verbose=0)'''
    l, a = model.evaluate(
        X,
        Y,
        verbose=verbose
    )
    return l, a
