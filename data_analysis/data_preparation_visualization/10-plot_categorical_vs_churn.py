#!/usr/bin/env python3
"""plot_continuous_distributions
"""

import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    '''plot_categorical_vs_churn'''
    counts = df.groupby(col)['Churn'].value_counts(normalize=True)\
        .reset_index().query("Churn == 'Yes'")
    plt.figure(figsize=(12, 8))
    plt.bar(counts[col], counts['proportion'])
    plt.title(f'Churn Rate by {col}')
    plt.ylabel('Churn Rate')
    plt.xticks(rotation=45)
    return None
