#!/usr/bin/env python3
"""Tree-Based Models
"""

from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    """evaluate
    """
    report = metrics.classification_report(
        true_labels,
        predicted_labels,
        target_names=class_names
    )
    return report
