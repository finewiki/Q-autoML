from dataclasses import dataclass
from typing import List, Dict

@dataclass
class DataConfig:
    # Feature engineering parameters
    technical_indicators: List[str] = [
        'SMA_20', 'SMA_50', 'EMA_20',
        'RSI', 'MACD', 'ATR',
        'Bollinger_Upper', 'Bollinger_Lower'
    ]
    
    # Data preprocessing parameters
    fill_method: str = 'ffill'
    scaling_method: str = 'standard'
    outlier_threshold: float = 3.0
    
    # Train-test split parameters
    test_size: float = 0.2
    validation_size: float = 0.1
    random_state: int = 42