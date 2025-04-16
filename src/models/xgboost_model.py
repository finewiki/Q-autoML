import xgboost as xgb
from typing import Dict, Any

class FinancialXGBoost:
    def __init__(self, params: Dict[str, Any] = None):
        self.params = params or {
            'objective': 'binary:logistic',
            'eval_metric': 'auc',
            'tree_method': 'hist'
        }
        self.model = xgb.XGBModel(**self.params)
        
    def fit(self, X, y, eval_set=None):
        self.model.fit(X, y, eval_set=eval_set)
        return self