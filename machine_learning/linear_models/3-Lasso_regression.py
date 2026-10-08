#!/usr/bin/env python3
"""Linear Regression Project
"""

from sklearn import linear_model


def lasso_regression(random_state):
    '''ridge_regression'''
    return linear_model.Lasso(random_state=random_state)
