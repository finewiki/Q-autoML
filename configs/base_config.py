from dataclasses import dataclass
from typing import Optional

@dataclass
class BaseConfig:
    project_name: str = "Q-autoML"
    random_state: int = 42
    verbose: bool = True
    log_level: str = "INFO"
    output_dir: str = "/Users/usermail/Desktop/Q-autoML/outputs"
    model_dir: str = "/Users/usermail/Desktop/Q-autoML/models"
    cache_dir: str = "/Users/usermail/Desktop/Q-autoML/cache"
