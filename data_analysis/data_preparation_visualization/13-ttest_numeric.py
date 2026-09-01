#!/usr/bin/env python3
"""plot_continuous_distributions
"""

import pandas as pd
from scipy import stats

def ttest_numeric(df):
    '''def ttest_numeric(df):'''
    cols = df.select_dtypes(include='number').columns.tolist()
    res = {}
    for f in cols:
        group_A = df.loc(df['Churn'] == "Yes", f)
        group_B = df.loc(df['Churn'] == "No", f)
        t, p = stats.ttest_ind(group_A, group_B, equal_var=False)
        res[f] = p
    return res
