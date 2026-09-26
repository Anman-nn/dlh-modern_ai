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
        n_clusters=n_clusters
    )

    labels = model.fit_predict(X)
    score = metrics.silhouette_score(X, labels)

    return model, X, score
