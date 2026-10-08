#!/usr/bin/env python3
"""Tree-Based Models
"""

import numpy as np


def feature_importance(rf):
    '''importance'''
    index=X_train.columns
    return rf.feature_importances_, 