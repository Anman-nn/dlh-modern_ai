#!/usr/bin/env python3
'''Data Preparation and Visualization'''

import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    '''visualizes missing values in a DataFrame'''
    plt.figure(figsize=(12, 8))

    y = df.columns
    x = df.isna().to_numpy()
    plt.scatter(x, y)
    plt.title('Missingness Plot')
    plt.tight_layout()
    plt.show()
    