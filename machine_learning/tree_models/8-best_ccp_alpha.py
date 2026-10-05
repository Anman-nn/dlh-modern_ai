#!/usr/bin/env python3
"""Tree-Based Models
"""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    '''get best'''
    m_train_scores = max(test_scores)
    indices = [i for i, value in enumerate(test_scores) if value == m_train_scores]
    if len(indices)>1:
        dif = {}
        for i, value in enumerate(indices):
            dif[value] = abs(train_scores[value] - test_scores[value])
        min_value = min(dif.values())
        indices = [i for i, val in dif.items() if val == min_value]
        if len(indices)>1:
            alphas = [ccp_alphas[i] for i in indices]
            indices = []
            indices.append(ccp_alphas.index(max(alphas)))

    i = indices[0]
    best_alpha = ccp_alphas[i]
    best_clf = clfs[i]

    return best_alpha, best_clf
