#!/usr/bin/env python3
"""Enhancing Deep Learning Models
"""

import keras_tuner


def initiate_tuner(
        tuner_type, build_model, seed,
        hyperband_iterations, max_trials, objective
        ):
    '''init tuner'''
    if tuner_type == "Hyperband":
        tuner = keras_tuner.Hyperband(
            hypermodel=build_model,
            objective=objective,
            hyperband_iterations=hyperband_iterations,
            seed=seed
        )

    elif tuner_type == 'RandomSearch':
        tuner = keras_tuner.RandomSearch(
            hypermodel=build_model,
            objective=objective,
            max_trials=max_trials,
            seed=seed
            )

    elif tuner_type == "BayesianOptimization":
        tuner = keras_tuner.RandomSearch(
            hypermodel=build_model,
            objective=objective,
            max_trials=max_trials,
            seed=seed
        )

    return tuner
