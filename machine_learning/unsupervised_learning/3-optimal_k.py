#!/usr/bin/env python3
"""Unsupervised Learning
"""

from sklearn import metrics
K_Means = __import__('2-k_means').K_Means


def optimal_k(X, max_clusters, random_state):
    '''optimal_k(X, max_clusters, random_state)'''

    return list(range(2,10))
