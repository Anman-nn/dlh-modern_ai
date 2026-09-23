#!/usr/bin/env python3
"""Unsupervised Learning
"""

from sklearn import preprocessing


def Standardize(X):
    '''def scale_numeric(df):'''

    scaler = preprocessing.StandardScaler()

    res = scaler.fit_transform(X)

    return res
