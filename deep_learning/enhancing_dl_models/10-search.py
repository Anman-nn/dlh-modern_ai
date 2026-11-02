#!/usr/bin/env python3
"""Enhancing Deep Learning Models
"""

import keras_tuner


def search_and_return_best_model(
        tuner, x_train, y_train, epochs,
        validation_split, verbose=0
        ):
    '''search_and_return_best_model'''

    s = tuner.search(
        x_train,
        y_train,
        epochs=epochs,
        validation_split=validation_split,
        verbose=verbose
        )

    best = tuner.get_best_hyperparameters(num_trials=1)[0]

    return best
