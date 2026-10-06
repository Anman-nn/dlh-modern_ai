#!/usr/bin/env python3
"""Linear Regression Project
"""

from sklearn import metrics
import numpy as np


def evaluation_metrics_for_regression(y_true, y_pred):
    '''sldjhfsjdh'''
    mse = metrics.mean_squared_error(y_true, y_pred)
    rmse = metrics.root_mean_squared_error(y_true, y_pred)
    mae = metrics.mean_absolute_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)
    return (mse, rmse, mae, r2)
