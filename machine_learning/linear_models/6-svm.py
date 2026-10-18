#!/usr/bin/env python3
"""Linear Regression Project
"""

from sklearn import svm


def get_SVM_model(name, random_state):
    '''get_SVM_model'''
    model = svm.SVC(kernel=name, random_state=random_state)
    return model
