import optuna
from typing import Dict, Any, Callable
import numpy as np

class FinancialHyperparameterTuner:
    def __init__(
        self,
        objective_func: Callable,
        param_space: Dict[str, Any],
        n_trials: int = 100,
        timeout: int = 3600
    ):
        self.objective_func = objective_func
        self.param_space = param_space
        self.n_trials = n_trials
        self.timeout = timeout
        
    def optimize(self) -> Dict[str, Any]:
        """
        Run Optuna optimization
        """
        study = optuna.create_study(
            direction="maximize",
            sampler=optuna.samplers.TPESampler(seed=42)
        )
        
        study.optimize(
            self.objective_func,
            n_trials=self.n_trials,
            timeout=self.timeout
        )
        
        return study.best_params