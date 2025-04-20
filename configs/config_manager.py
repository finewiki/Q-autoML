from typing import Dict, Any
import yaml
import os
from .base_config import BaseConfig
from .data_config import DataConfig
from .model_config import ModelConfig
from .training_config import TrainingConfig

class ConfigManager:
    def __init__(self, config_path: str = None):
        self.base_config = BaseConfig()
        self.data_config = DataConfig()
        self.model_config = ModelConfig()
        self.training_config = TrainingConfig()
        
        if config_path and os.path.exists(config_path):
            self.load_from_yaml(config_path)
    
    def load_from_yaml(self, config_path: str) -> None:
        with open(config_path, 'r') as f:
            config_dict = yaml.safe_load(f)
            
        for key, value in config_dict.get('base_config', {}).items():
            setattr(self.base_config, key, value)
            
        for key, value in config_dict.get('data_config', {}).items():
            setattr(self.data_config, key, value)
            
        for key, value in config_dict.get('model_config', {}).items():
            setattr(self.model_config, key, value)
            
        for key, value in config_dict.get('training_config', {}).items():
            setattr(self.training_config, key, value)
    
    def save_to_yaml(self, config_path: str) -> None:
        config_dict = {
            'base_config': self.base_config.__dict__,
            'data_config': self.data_config.__dict__,
            'model_config': self.model_config.__dict__,
            'training_config': self.training_config.__dict__
        }
        
        with open(config_path, 'w') as f:
            yaml.dump(config_dict, f, default_flow_style=False)