from typing import Dict, List

SUPPORTED_MODELS: List[str] = [
    "xgboost",
    "lightgbm",
    "catboost",
    "random_forest"
]

DEFAULT_HYPERPARAMETERS: Dict[str, Dict] = {
    "xgboost": {
        "max_depth": 6,
        "learning_rate": 0.1,
        "n_estimators": 100
    },
    "lightgbm": {
        "num_leaves": 31,
        "learning_rate": 0.1,
        "n_estimators": 100
    }
}

METRIC_NAMES: List[str] = [
    "accuracy",
    "precision",
    "recall",
    "f1",
    "auc",
    "sharpe_ratio",
    "max_drawdown"
]