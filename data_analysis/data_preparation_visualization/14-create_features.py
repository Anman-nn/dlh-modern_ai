#!/usr/bin/env python3
"""plot_continuous_distributions
"""

import pandas as pd


def create_features(df):
    '''def create_features(df):'''
    service_cols = [
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
    ]

    yes_service_cols = [
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
    ]

    df["NumServices"] = df[yes_service_cols].eq("Yes").sum(axis=1)
    df["NumServices"] += df["InternetService"].isin(["DSL", "Fiber optic"])

    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 60, float("inf")],
        labels=["0-12", "13-24", "25-48", "49-60", "60+"],
        include_lowest=False
    )

    df = df.drop(columns=service_cols + ["tenure"])

    return df
