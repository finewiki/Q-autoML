from typing import Dict, Any
import os
import yaml

class BaseConfig:
    def __init__(self):
        self.project_root = "/Users/usermail/Desktop/autoML"
        self.data_dir = os.path.join(self.project_root, "data")
        self.models_dir = os.path.join(self.project_root, "models")
        
        # Data directories
        self.raw_data_dir = os.path.join(self.data_dir, "raw")
        self.processed_data_dir = os.path.join(self.data_dir, "processed")
        self.external_data_dir = os.path.join(self.data_dir, "external")
        
        # Logging settings
        self.log_level = "INFO"
        self.log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        self.log_dir = os.path.join(self.project_root, "logs")