import numpy as np
import pandas as pd
from typing import Tuple, Optional

class FinancialDataGenerator:
    def __init__(self, n_samples: int = 1000, n_features: int = 10):
        self.n_samples = n_samples
        self.n_features = n_features
        
    def generate_classification_data(self) -> Tuple[pd.DataFrame, pd.Series]:
        X = np.random.randn(self.n_samples, self.n_features)
        y = (X[:, 0] + X[:, 1] > 0).astype(int)
        
        feature_names = [f"feature_{i}" for i in range(self.n_features)]
        return pd.DataFrame(X, columns=feature_names), pd.Series(y)
        
    def generate_regression_data(self) -> Tuple[pd.DataFrame, pd.Series]:
        X = np.random.randn(self.n_samples, self.n_features)
        y = np.sum(X[:, :3], axis=1) + np.random.randn(self.n_samples) * 0.1
        
        feature_names = [f"feature_{i}" for i in range(self.n_features)]
        return pd.DataFrame(X, columns=feature_names), pd.Series(y)