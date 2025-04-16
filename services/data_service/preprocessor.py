import pandas as pd
import numpy as np
from typing import List, Dict, Any

class FinancialPreprocessor:
    def __init__(self):
        self.technical_indicators = [
            'SMA', 'EMA', 'RSI', 'MACD'
        ]
    
    def calculate_technical_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        # Simple Moving Average
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        
        # Exponential Moving Average
        df['EMA_20'] = df['Close'].ewm(span=20).mean()
        
        # RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        return df