#!/usr/bin/env python3
"""Tree-Based Models
"""

from sklearn import tree


def draw(clf, feature_names, class_names):
    """draw
    """
    res = tree.export_text(
        clf,
        feature_names=feature_names,
        class_names=class_names,
        decimals=2)
    print(res)
    return None
