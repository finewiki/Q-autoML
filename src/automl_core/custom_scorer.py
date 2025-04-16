from typing import Callable, Dict
import numpy as np

class FinancialScorer:
    @staticmethod
    def risk_adjusted_return(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        returns = y_pred - y_true
        return np.mean(returns) / (np.std(returns) + 1e-6)
    
    @staticmethod
    def profit_factor(y_true: np.ndarray, y_pred: np.ndarray) -> float:
        gains = np.sum(np.maximum(y_pred - y_true, 0))
        losses = np.sum(np.maximum(y_true - y_pred, 0))
        return gains / (losses + 1e-6)
    
    @staticmethod
    def get_scorer(metric_name: str) -> Callable:
        metrics = {
            'risk_adjusted_return': FinancialScorer.risk_adjusted_return,
            'profit_factor': FinancialScorer.profit_factor
        }
        return metrics.get(metric_name)