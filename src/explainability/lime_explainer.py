from lime import lime_tabular
import pandas as pd
import numpy as np
from typing import List, Dict, Optional

class LimeExplainer:
    def __init__(
        self,
        model,
        feature_names: List[str],
        categorical_features: Optional[List[int]] = None,
        class_names: Optional[List[str]] = None
    ):
        self.model = model
        self.feature_names = feature_names
        self.categorical_features = categorical_features or []
        self.class_names = class_names
        self.explainer = None
        
    def fit(self, X: pd.DataFrame):
        """
        Initialize LIME explainer
        """
        self.explainer = lime_tabular.LimeTabularExplainer(
            X.values,
            feature_names=self.feature_names,
            class_names=self.class_names,
            categorical_features=self.categorical_features,
            mode='classification' if self.class_names else 'regression'
        )
        
    def explain_instance(
        self,
        instance: np.ndarray,
        num_features: int = 10
    ) -> Dict[str, float]:
        """
        Generate explanation for a single instance
        """
        exp = self.explainer.explain_instance(
            instance,
            self.model.predict_proba if self.class_names else self.model.predict,
            num_features=num_features
        )
        
        explanation = {}
        for feature, importance in exp.as_list():
            explanation[feature] = importance
            
        return explanation
    
    def explain_dataset(
        self,
        X: pd.DataFrame,
        sample_size: int = 100
    ) -> List[Dict[str, float]]:
        """
        Generate explanations for multiple instances
        """
        if sample_size > len(X):
            sample_size = len(X)
            
        sample_indices = np.random.choice(len(X), sample_size, replace=False)
        explanations = []
        
        for idx in sample_indices:
            explanation = self.explain_instance(X.iloc[idx].values)
            explanations.append(explanation)
            
        return explanations