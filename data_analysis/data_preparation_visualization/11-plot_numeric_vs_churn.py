#!/usr/bin/env python3
"""plot_continuous_distributions
"""

import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    '''def plot_numeric_vs_churn(df, col):'''
    plt.figure(figsize=(12, 8))

    churn_yes = df[df["Churn"] == "Yes"][col].dropna()
    churn_no = df[df["Churn"] == "No"][col].dropna()

    plt.hist(churn_no, bins=30, alpha=0.5, label="No")
    plt.hist(churn_yes, bins=30, alpha=0.5, label="Yes")

    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)
    plt.legend(title="Churn")

    plt.show()
    return None