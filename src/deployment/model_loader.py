import joblib
import json
from typing import Tuple, Dict, Any
import os

class ModelLoader:
    def __init__(self, model_dir: str = "/Users/usermail/Desktop/autoML/models"):
        self.model_dir = model_dir
        
    def load_model(self, model_name: str) -> Tuple[Any, Dict]:
        """
        Load model and its metadata
        """
        model_path = os.path.join(self.model_dir, f"{model_name}.pkl")
        meta_path = os.path.join(self.model_dir, f"{model_name}_meta.json")
        
        if not os.path.exists(model_path) or not os.path.exists(meta_path):
            raise FileNotFoundError(f"Model {model_name} not found")
            
        model = joblib.load(model_path)
        
        with open(meta_path, 'r') as f:
            metadata = json.load(f)
            
        return model, metadata
    
    def save_model(self, model: Any, metadata: Dict, model_name: str):
        """
        Save model and its metadata
        """
        os.makedirs(self.model_dir, exist_ok=True)
        
        model_path = os.path.join(self.model_dir, f"{model_name}.pkl")
        meta_path = os.path.join(self.model_dir, f"{model_name}_meta.json")
        
        joblib.dump(model, model_path)
        
        with open(meta_path, 'w') as f:
            json.dump(metadata, f)