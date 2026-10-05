#!/usr/bin/env python3
"""Tree-Based Models
"""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    '''get best'''
    max_test_score = max(test_scores)

    indices = [
        i for i, score in enumerate(test_scores)
        if score == max_test_score
    ]

    if len(indices) > 1:
        differences = {
            i: abs(train_scores[i] - test_scores[i])
            for i in indices
        }

        min_difference = min(differences.values())

        indices = [
            i for i in indices
            if differences[i] == min_difference
        ]

    if len(indices) > 1:
        best_index = max(
            indices,
            key=lambda i: ccp_alphas[i]
        )
    else:
        best_index = indices[0]

    best_alpha = ccp_alphas[best_index]
    best_clf = clfs[best_index]

    return best_alpha, best_clf
