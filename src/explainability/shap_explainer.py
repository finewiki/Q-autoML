import shap
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Union
import matplotlib.pyplot as plt

class ShapExplainer:
    def __init__(self, model, model_type: str = "tree"):
        self.model = model
        self.model_type = model_type
        self.explainer = None
        self.shap_values = None
        
    def fit(self, X: pd.DataFrame):
        """
        Initialize SHAP explainer based on model type
        """
        if self.model_type == "tree":
            self.explainer = shap.TreeExplainer(self.model)
        else:
            self.explainer = shap.KernelExplainer(self.model.predict, X)
            
        self.shap_values = self.explainer.shap_values(X)
        
    def get_feature_importance(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate global feature importance using SHAP values
        """
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': np.abs(self.shap_values).mean(0)
        })
        return feature_importance.sort_values('importance', ascending=False)
    
    def plot_summary(self, X: pd.DataFrame):
        """
        Generate SHAP summary plot
        """
        shap.summary_plot(self.shap_values, X)
        
    def explain_prediction(
        self,
        X: pd.DataFrame,
        row_index: int
    ) -> Dict[str, float]:
        """
        Explain individual prediction
        """
        explanation = {}
        for idx, col in enumerate(X.columns):
            explanation[col] = self.shap_values[row_index][idx]
        return explanation