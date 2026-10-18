#!/usr/bin/env python3
"""Linear Regression Project
"""

from sklearn import svm


def get_SVM_model(name, random_state):
    '''Logistic_Regression_Model(random_state)'''
    model = svm.SVC.LogisticRegressionCV(kernel=name, random_state=random_state)
    return model
