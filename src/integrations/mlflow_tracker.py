import mlflow
from typing import Dict, Any

class MLFlowTracker:
    def __init__(self, experiment_name: str):
        mlflow.set_experiment(experiment_name)
        
    def log_params(self, params: Dict[str, Any]):
        with mlflow.start_run():
            mlflow.log_params(params)
            
    def log_metrics(self, metrics: Dict[str, float]):
        with mlflow.start_run():
            mlflow.log_metrics(metrics)
            
    def log_model(self, model: Any, model_name: str):
        with mlflow.start_run():
            mlflow.sklearn.log_model(model, model_name)