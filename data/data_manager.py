import pandas as pd
import numpy as np
from typing import Dict, List, Optional
import os
import yfinance as yf
from datetime import datetime, timedelta

class FinancialDataManager:
    def __init__(self):
        self.raw_dir = "/Users/usermail/Desktop/autoML/data/raw"
        self.processed_dir = "/Users/usermail/Desktop/autoML/data/processed"
        self.external_dir = "/Users/usermail/Desktop/autoML/data/external"
        
        # Create directories if they don't exist
        for directory in [self.raw_dir, self.processed_dir, self.external_dir]:
            os.makedirs(directory, exist_ok=True)
    
    def fetch_stock_data(
        self,
        symbol: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> pd.DataFrame:
        """Fetch stock data and save to raw directory"""
        if not start_date:
            start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
        if not end_date:
            end_date = datetime.now().strftime('%Y-%m-%d')
        
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start_date, end=end_date)
        
        # Save raw data
        raw_path = os.path.join(self.raw_dir, f"{symbol}_{start_date}_{end_date}.csv")
        data.to_csv(raw_path)
        
        return data
    
    def process_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Process raw data with technical indicators and features"""
        df = df.copy()
        
        # Technical indicators
        df['Returns'] = df['Close'].pct_change()
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['Volatility'] = df['Returns'].rolling(window=20).std()
        
        # Price features
        df['Price_Range'] = df['High'] - df['Low']
        df['Price_Change'] = df['Close'] - df['Open']
        
        # Volume features
        df['Volume_MA5'] = df['Volume'].rolling(window=5).mean()
        df['Volume_Change'] = df['Volume'].pct_change()
        
        # Clean up
        df = df.dropna()
        
        return df
    
    def save_processed_data(self, df: pd.DataFrame, filename: str):
        """Save processed data"""
        processed_path = os.path.join(self.processed_dir, filename)
        df.to_csv(processed_path, index=True)
        
    def load_data(self, filename: str, data_type: str = 'processed') -> pd.DataFrame:
        """Load data from either raw or processed directory"""
        directory = self.processed_dir if data_type == 'processed' else self.raw_dir
        filepath = os.path.join(directory, filename)
        return pd.read_csv(filepath)