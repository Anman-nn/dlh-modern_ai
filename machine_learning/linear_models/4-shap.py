#!/usr/bin/env python3
"""Linear Regression Project
"""

import shap

def get_shap_explainer_and_values(model, X_train, X_test):
    """shap
    """
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)

    return explainer, shap_values
