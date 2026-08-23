#!/usr/bin/env python3
'''Data Preparation and Visualization'''

import pandas as pd


def convert_columns(df):
    '''conversion'''
    df.TotalCharges = pd.to_numeric(df.TotalCharges, errors='coerce')
    df["SeniorCitizen"] = df["SeniorCitizen"].map({"0": "No", "1": "Yes"}).fillna("No")
    return df
