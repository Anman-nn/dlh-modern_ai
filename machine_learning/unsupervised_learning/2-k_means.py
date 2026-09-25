#!/usr/bin/env python3
"""Unsupervised Learning
"""

from sklearn import cluster


def K_Means(X, n_clusters, random_state):
    '''K_Means(X, n_clusters, random_state)'''

    kmeans = cluster.KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init='auto'
    )
    kmeans.fit(X)
    return kmeans
