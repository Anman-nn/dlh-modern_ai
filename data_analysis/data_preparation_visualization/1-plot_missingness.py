#!/usr/bin/env python3
'''Data Preparation and Visualization'''

import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    '''visualizes missing values in a DataFrame'''
    missing = df.isna()
    for y_pos, column in enumerate(df.columns):
        x_values = df.index[missing[column]]
        y_values = [y_pos] * len(x_values)

        plt.scatter(x_values, y_values, marker="|")

    plt.yticks(range(len(df.columns)), df.columns)
    plt.show()

    return None
