#!/usr/bin/env python3
"""plot_continuous_distributions
"""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """plot_correlation_heatmap
    """
    plt.figure(figsize=(6, 5))

    corr = df.select_dtypes(include="number").corr()

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        vmin=-1,
        vmax=1
    )
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()

    return None
