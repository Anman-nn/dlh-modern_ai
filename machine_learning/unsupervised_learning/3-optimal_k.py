#!/usr/bin/env python3
"""Unsupervised Learning
"""

from sklearn import metrics
K_Means = __import__('2-k_means').K_Means


def optimal_k(X, max_clusters, random_state):
    '''optimal_k(X, max_clusters, random_state)'''
    K = range(2, max_clusters+1)
    fits = []
    inertia_values = []
    silhouette_values = []
    ks = []

    for k in K:
        # train the model for current value of k on training data
        model = K_Means(X, k, random_state)
        
        # append the model to fits
        fits.append(model)
        
        inertia_values.append(model.inertia_)

        # Append the silhouette score to scores
        silhouette_values.append(metrics.silhouette_score(
            X, model.labels_, metric='euclidean'))

        ks.append(k)

    return ks, inertia_values, silhouette_values
