import pandas as pd
import numpy as np
from datetime import datetime
import os
from typing import Dict, List

class StockDataProcessor:
    def __init__(self):
        self.raw_dir = "/Users/usermail/Desktop/autoML/data/raw"
        self.processed_dir = "/Users/usermail/Desktop/autoML/data/processed"
        os.makedirs(self.processed_dir, exist_ok=True)

    def process_stock_data(self, symbol: str, raw_filename: str) -> pd.DataFrame:
        # Read raw data
        raw_path = os.path.join(self.raw_dir, raw_filename)
        df = pd.read_csv(raw_path, index_col=0, parse_dates=True)
        
        # Calculate technical indicators
        df['Daily_Return'] = df['Close'].pct_change()
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
        
        # Momentum indicators
        df['RSI'] = self._calculate_rsi(df['Close'])
        df['MACD'] = self._calculate_macd(df['Close'])
        
        # Volatility indicators
        df['ATR'] = self._calculate_atr(df[['High', 'Low', 'Close']])
        df['Bollinger_Upper'], df['Bollinger_Lower'] = self._calculate_bollinger_bands(df['Close'])
        
        # Volume indicators
        df['Volume_MA'] = df['Volume'].rolling(window=20).mean()
        df['Volume_Ratio'] = df['Volume'] / df['Volume_MA']
        
        # Save processed data
        timestamp = datetime.now().strftime('%Y%m%d')
        processed_filename = f"{symbol}_processed_{timestamp}.csv"
        processed_path = os.path.join(self.processed_dir, processed_filename)
        df.to_csv(processed_path)
        
        return df
    
    def _calculate_rsi(self, prices: pd.Series, period: int = 14) -> pd.Series:
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))
    
    def _calculate_macd(self, prices: pd.Series) -> pd.Series:
        exp1 = prices.ewm(span=12, adjust=False).mean()
        exp2 = prices.ewm(span=26, adjust=False).mean()
        return exp1 - exp2
    
    def _calculate_atr(self, data: pd.DataFrame) -> pd.Series:
        high = data['High']
        low = data['Low']
        close = data['Close']
        tr1 = high - low
        tr2 = abs(high - close.shift())
        tr3 = abs(low - close.shift())
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        return tr.rolling(window=14).mean()
    
    def _calculate_bollinger_bands(
        self,
        prices: pd.Series,
        window: int = 20,
        num_std: float = 2
    ) -> tuple:
        sma = prices.rolling(window=window).mean()
        std = prices.rolling(window=window).std()
        upper_band = sma + (std * num_std)
        lower_band = sma - (std * num_std)
        return upper_band, lower_band

if __name__ == "__main__":
    processor = StockDataProcessor()
    # Process latest raw data files
    raw_files = [f for f in os.listdir(processor.raw_dir) if f.endswith('.csv')]
    for raw_file in raw_files:
        symbol = raw_file.split('_')[0]
        processor.process_stock_data(symbol, raw_file)