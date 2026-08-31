#!/usr/bin/env python3
"""plot_continuous_distributions
"""

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    '''chi square'''
    f = df.select_dtypes(include="object").columns.tolist()
    f.remove('Churn')
    res = {}
    for col in f:
        table = pd.crosstab(df[col], df["Churn"])
        chi2, p, dof, expected = stats.chi2_contingency(table)
        res[col] = p
    return res
