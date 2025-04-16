import yaml
import os
from typing import Dict, Any
from .base_config import BaseConfig
from .data_config import DataConfig

class ConfigLoader:
    def __init__(self):
        self.base_config = BaseConfig()
        self.data_config = DataConfig()
        self.model_config = self._load_yaml('model_config.yaml')
        self.service_config = self._load_yaml('service_config.yaml')
        
    def _load_yaml(self, filename: str) -> Dict[str, Any]:
        config_path = os.path.join(self.base_config.project_root, 'configs', filename)
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def get_model_params(self, model_type: str) -> Dict[str, Any]:
        return self.model_config.get(model_type, {})