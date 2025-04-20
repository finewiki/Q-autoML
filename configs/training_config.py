from dataclasses import dataclass
from typing import Optional, List

@dataclass
class TrainingConfig:
    # Training settings
    device: str = "cpu"
    num_workers: int = 4
    pin_memory: bool = True
    
    # Callbacks and monitoring
    enable_checkpointing: bool = True
    checkpoint_freq: int = 5
    
    # Metrics to monitor
    metrics: List[str] = None
    primary_metric: str = "val_loss"
    
    # MLflow tracking
    enable_mlflow: bool = False
    mlflow_tracking_uri: Optional[str] = None
    
    def __post_init__(self):
        if self.metrics is None:
            self.metrics = ["loss", "mae", "rmse"]