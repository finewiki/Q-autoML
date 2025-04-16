import pandas as pd
import numpy as np
from typing import Dict, List, Any
from ..explainability.shap_explainer import ShapExplainer

class Predictor:
    def __init__(self):
        self.model = None
        self.explainer = None
        self.feature_names = None
        self.model_type = None
        self.model_metrics = None
        
    def load(self, model: Any, metadata: Dict):
        """
        Load model and initialize explainer
        """
        self.model = model
        self.model_type = metadata.get('model_type')
        self.feature_names = metadata.get('feature_names')
        self.model_metrics = metadata.get('metrics')
        
        self.explainer = ShapExplainer(self.model)
        
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """
        Make predictions
        """
        if self.model is None:
            raise ValueError("Model not loaded")
            
        return self.model.predict(X)
    
    def explain(self, X: pd.DataFrame) -> Dict[str, float]:
        """
        Generate explanation for predictions
        """
        if self.explainer is None:
            raise ValueError("Explainer not initialized")
            
        return self.explainer.explain_prediction(X, 0)