#!/usr/bin/env python3
"""Unsupervised Learning
"""

from sklearn import decomposition


def Apply_PCA(X, n_components, random_state):
    '''Apply_PCA(X, n_components, random_state)'''
    pca = decomposition.PCA(n_components)

    return pca.fit_transform(X), pca
