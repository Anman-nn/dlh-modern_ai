#!/usr/bin/env python3
"""Tree-Based Models
"""

from sklearn import tree
train_tree = __import__('1-train').train_tree


def prune_and_evaluate_trees(
        X_train, y_train, X_test, y_test,
        ccp_alphas, random_state, min_samples_leaf, 
        min_samples_split
):
    """prune_and_evaluate_trees
    """
    clfs = []
    train_scores = []
    test_scores = []
    for alpha in ccp_alphas:
        clf = tree.DecisionTreeClassifier(
            ccp_alpha=alpha,
            random_state=random_state,
            min_samples_leaf=min_samples_leaf,
            min_samples_split=min_samples_split
        )
        train_tree(clf, X_train, y_train)
        train_score = clf.score(
            X_train,
            y_train
        )
        test_score = clf.score(
            X_test,
            y_test,
        )
        clfs.append(clf)
        train_scores.append(train_score)
        test_scores.append(test_score)
    return clfs, train_scores, test_scores
