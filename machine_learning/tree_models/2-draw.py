#!/usr/bin/env python3
"""Tree-Based Models
"""

from sklearn import tree


def draw(clf, feature_names, class_names):
    """draw"""
    tree.plot_tree(
        clf,
        feature_names=feature_names,
        class_names=class_names)
    return None
