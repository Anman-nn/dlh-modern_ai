#!/usr/bin/env python3
'''Data Preparation and Visualization'''


import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    """
    plt.figure(figsize=(12, 8))
    plt.title('Churn Distribution')
    plt.ylabel('Count')
    plt.bar(["No", "Yes"], df.Churn.value_counts(), 
            color=["skyblue", "salmon"])
    plt.show()
