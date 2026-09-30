#!/usr/bin/env python3
"""Tree-Based Models
"""


def get_pruning_path(clf, X, y):
    """get_pruning_path(clf, X, y)
    """
    path = clf.cost_complexity_pruning_path(X, y)
    return path.ccp_alphas, path.impurities
