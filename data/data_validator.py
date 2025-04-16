import pandas as pd
from typing import List, Dict
import numpy as np

class DataValidator:
    @staticmethod
    def validate_stock_data(df: pd.DataFrame) -> bool:
        """Validate stock data structure and content"""
        required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        
        # Check required columns
        if not all(col in df.columns for col in required_columns):
            return False
            
        # Check for missing values
        if df[required_columns].isnull().any().any():
            return False
            
        # Check data types
        numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        if not all(pd.api.types.is_numeric_dtype(df[col]) for col in numeric_columns):
            return False
            
        return True
    
    @staticmethod
    def validate_features(df: pd.DataFrame) -> Dict[str, bool]:
        """Validate calculated features"""
        feature_checks = {
            'Returns': lambda x: not x.isnull().all(),
            'SMA_20': lambda x: not x.isnull().all(),
            'Volatility': lambda x: not x.isnull().all(),
            'Price_Range': lambda x: (x >= 0).all()
        }
        
        results = {}
        for feature, check_func in feature_checks.items():
            if feature in df.columns:
                results[feature] = check_func(df[feature])
            else:
                results[feature] = False
                
        return results