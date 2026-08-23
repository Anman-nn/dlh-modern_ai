#!/usr/bin/env python3
'''Data Preparation and Visualization'''


def clean_total_charges(df, method='drop'):
    '''conversion'''
    import pandas as pd
    if method == 'drop':
        df.dropna(subset=["TotalCharges"], inplace=True)
    elif method == 'median':
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df['TotalCharges'] = df['TotalCharges'].fillna(1397.475)
    elif method == 'impute':
        df['TotalCharges'] = df['TotalCharges'].fillna(df['MonthlyCharges']*df['tenure'])
    return df
 