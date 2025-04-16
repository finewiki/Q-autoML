from catboost import CatBoostClassifier, CatBoostRegressor
from typing import Dict, Any

class FinancialCatBoost:
    def __init__(self, task: str = 'classification', params: Dict[str, Any] = None):
        self.params = params or {}
        self.model = (CatBoostClassifier(**self.params) if task == 'classification' 
                     else CatBoostRegressor(**self.params))
        
    def fit(self, X, y, eval_set=None):
        self.model.fit(X, y, eval_set=eval_set)
        return self