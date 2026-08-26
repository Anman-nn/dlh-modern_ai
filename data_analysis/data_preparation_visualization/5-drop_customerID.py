#!/usr/bin/env python3
'''Data Preparation and Visualization'''


def drop_customerID(df):
    '''def drop_customerID(df):'''
    df = df.drop('customerID', axis=1)
    return df
