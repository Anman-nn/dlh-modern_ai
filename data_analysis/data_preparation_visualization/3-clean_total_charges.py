#!/usr/bin/env python3
'''Data Preparation and Visualization'''


def clean_total_charges(df, method='drop'):
    '''conversion'''
    if method == 'drop':
        df.dropna(subset=["TotalCharges"], inplace=True)
    elif method == 'median':
        df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
    elif method == 'impute':
        df['TotalCharges'] = df['TotalCharges'].fillna(df['MonthlyCharges']*df['tenure'])
    return df
 