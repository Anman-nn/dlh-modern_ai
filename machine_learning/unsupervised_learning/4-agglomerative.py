#!/usr/bin/env python3
"""Unsupervised Learning
"""

from sklearn import cluster
from sklearn import metrics
Apply_PCA = __import__('1-pca').Apply_PCA


def Agglomerative_Clustering(
    X,
    n_clusters,
    random_state,
    n_components,
    use_pca_data=True
):
    """Agglomerative_Clustering"""

    if use_pca_data:
        X, pca_model = Apply_PCA(
            X,
            n_components,
            random_state
        )

    model = cluster.AgglomerativeClustering(
        n_clusters=n_clusters)

    model.fit(X)

    if n_clusters == 1:
        score = None
    else:
        score = float(
            metrics.silhouette_score(X, model.labels_)
        )

    return model, X, score
