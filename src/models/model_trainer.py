from typing import Dict, Any, Optional
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator
import xgboost as xgb
import lightgbm as lgb
import catboost as cb

class FinancialModelTrainer:
    def __init__(
        self,
        model_type: str = "xgboost",
        params: Optional[Dict[str, Any]] = None,
        test_size: float = 0.2,
        random_state: int = 42
    ):
        self.model_type = model_type
        self.params = params or {}
        self.test_size = test_size
        self.random_state = random_state
        self.model = self._initialize_model()
        
    def _initialize_model(self) -> BaseEstimator:
        if self.model_type == "xgboost":
            return xgb.XGBRegressor(**self.params)
        elif self.model_type == "lightgbm":
            return lgb.LGBMRegressor(**self.params)
        elif self.model_type == "catboost":
            return cb.CatBoostRegressor(**self.params)
        else:
            raise ValueError(f"Unsupported model type: {self.model_type}")
    
    def train(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        validation_data: Optional[tuple] = None
    ):
        if validation_data is None:
            X_train, X_val, y_train, y_val = train_test_split(
                X, y,
                test_size=self.test_size,
                random_state=self.random_state
            )
        else:
            X_train, y_train = X, y
            X_val, y_val = validation_data
            
        self.model.fit(
            X_train, y_train,
            eval_set=[(X_val, y_val)],
            early_stopping_rounds=50,
            verbose=False
        )
        
        return self.model