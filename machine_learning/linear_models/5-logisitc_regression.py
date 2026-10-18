#!/usr/bin/env python3
"""Linear Regression Project
"""

from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    '''Logistic_Regression_Model(random_state)'''
    model = linear_model.LogisticRegression(random_state=random_state)
    return model
