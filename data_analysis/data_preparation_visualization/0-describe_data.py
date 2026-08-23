#!/usr/bin/env python3
'''Data Preparation and Visualization'''

import pandas as pd

df = pd.read_csv('Telco-Customer-Churn.csv')
shape = # your code here
data_types = # your code here
head = # your code here
missing_count = # your code here
duplicates = # your code here
print("Shape:", shape)
print("Dtypes:\n", data_types)
print("First rows:\n", head)
print("Missing values:\n", missing_count)
print("Duplicates:", duplicates)