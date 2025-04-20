from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class ModelConfig:
    model_type: str = "lightgbm"
    hyperparameters: Dict = None
    
    # Training parameters
    batch_size: int = 32
    num_epochs: int = 100
    early_stopping_rounds: int = 10
    
    # Model architecture
    hidden_layers: List[int] = None
    dropout_rate: float = 0.2
    
    # Optimization parameters
    learning_rate: float = 0.001
    optimizer: str = "adam"
    loss_function: str = "mse"
    
    def __post_init__(self):
        if self.hyperparameters is None:
            self.hyperparameters = {}
        if self.hidden_layers is None:
            self.hidden_layers = [64, 32]