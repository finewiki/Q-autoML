from typing import Dict, List, Optional
import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_squared_error, mean_absolute_error, r2_score
)

class FinancialModelEvaluator:
    def __init__(self, task_type: str = "classification"):
        self.task_type = task_type
        
    def evaluate(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        custom_metrics: Optional[List[str]] = None
    ) -> Dict[str, float]:
        metrics = {}
        
        if self.task_type == "classification":
            metrics.update({
                "accuracy": accuracy_score(y_true, y_pred),
                "precision": precision_score(y_true, y_pred, average='weighted'),
                "recall": recall_score(y_true, y_pred, average='weighted'),
                "f1": f1_score(y_true, y_pred, average='weighted')
            })
        else:
            metrics.update({
                "mse": mean_squared_error(y_true, y_pred),
                "rmse": np.sqrt(mean_squared_error(y_true, y_pred)),
                "mae": mean_absolute_error(y_true, y_pred),
                "r2": r2_score(y_true, y_pred)
            })
            
        if custom_metrics:
            for metric in custom_metrics:
                if metric == "sharpe_ratio":
                    metrics["sharpe_ratio"] = self._calculate_sharpe_ratio(y_true, y_pred)
                elif metric == "max_drawdown":
                    metrics["max_drawdown"] = self._calculate_max_drawdown(y_true, y_pred)
                    
        return metrics
    
    def _calculate_sharpe_ratio(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        risk_free_rate: float = 0.02
    ) -> float:
        returns = y_pred - y_true
        excess_returns = returns - risk_free_rate
        return np.mean(excess_returns) / np.std(excess_returns)
    
    def _calculate_max_drawdown(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray
    ) -> float:
        cumulative = np.cumsum(y_pred - y_true)
        running_max = np.maximum.accumulate(cumulative)
        drawdown = running_max - cumulative
        return np.max(drawdown)