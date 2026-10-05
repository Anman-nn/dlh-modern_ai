#!/usr/bin/env python3
"""Tree-Based Models
"""

from sklearn import ensemble


def random_forest(n_estimators, random_state):
    '''random_forest(n_estimators, random_state)'''
    model = ensemble.RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )

    return model
