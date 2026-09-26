#!/usr/bin/env python3
"""Unsupervised Learning
"""

from sklearn import cluster
from sklearn import metrics
Apply_PCA = __import__('1-pca').Apply_PCA


def Agglomerative_Clustering(X, n_clusters, random_state, n_components, use_pca_data=True):
    if use_pca_data:
        X = Apply_PCA(X, n_components, random_state)
    model = cluster.AgglomerativeClustering(n_clusters = n_clusters)
    y_means = model.fit_predict(X)
    return y_means, X, metrics.silhouette_score(X, y_means)
