#!/usr/bin/env python3
"""plot_continuous_distributions
"""

from sklearn import preprocessing


def scale_numeric(df):
    '''def scale_numeric(df):'''
    df = df.copy()

    scaler = preprocessing.StandardScaler()

    df[["MonthlyCharges", "TotalCharges"]] = scaler.fit_transform(
        df[["MonthlyCharges", "TotalCharges"]]
    )

    return df
