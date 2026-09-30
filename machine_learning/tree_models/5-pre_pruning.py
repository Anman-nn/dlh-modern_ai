#!/usr/bin/env python3
"""Tree-Based Models
"""

from sklearn import model_selection


def prepruning(X, y, clf):
    """prepruning(X, y, clf)
    """

    param_grid = {
        "criterion": ["gini", "entropy"],
        "max_depth": range(2, 5),
        "min_samples_leaf": range(2, 5),
        "min_samples_split": range(2, 5),
    }
    s = model_selection.GridSearchCV(estimator=clf,
        param_grid=param_grid,
        scoring='accuracy',
        cv=5, n_jobs=-1
    )
    s.fit(X, y)
    return s.best_params_
