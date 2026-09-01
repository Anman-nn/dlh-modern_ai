#!/usr/bin/env python3
"""plot_continuous_distributions
"""

import pandas as pd
from sklearn import preprocessing

def encode_features(df):
    '''def encode_features(df):'''
    df = df.copy()

    churn_encoder = preprocessing.LabelEncoder()
    df["Churn"] = churn_encoder.fit_transform(df["Churn"])

    binary_cols = [
        "Partner",
        "Dependents",
        "PaperlessBilling",
        "SeniorCitizen",
    ]

    binary_encoder = preprocessing.OrdinalEncoder(
        categories=[["No", "Yes"]] * len(binary_cols)
    )
    df[binary_cols] = binary_encoder.fit_transform(df[binary_cols])

    tenure_encoder = preprocessing.OrdinalEncoder()
    df[["TenureGroup"]] = tenure_encoder.fit_transform(df[["TenureGroup"]])

    df = pd.get_dummies(
        df,
        columns=["Contract", "PaymentMethod"],
        drop_first=True
    )

    return df, churn_encoder, binary_encoder, tenure_encoder
