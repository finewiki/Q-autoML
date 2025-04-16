import yfinance as yf
import pandas as pd
import os
from datetime import datetime, timedelta
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataFetcher:
    def __init__(self):
        self.raw_data_path = "/Users/usermail/Desktop/autoML/data/raw"
        os.makedirs(self.raw_data_path, exist_ok=True)
        
    async def fetch_stock_data(
        self,
        symbol: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> str:
        try:
            if not start_date:
                start_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
            if not end_date:
                end_date = datetime.now().strftime("%Y-%m-%d")
                
            ticker = yf.Ticker(symbol)
            df = ticker.history(start=start_date, end=end_date)
            
            if df.empty:
                raise ValueError(f"No data found for symbol {symbol}")
            
            filename = f"{symbol}_{start_date}_{end_date}.csv"
            filepath = os.path.join(self.raw_data_path, filename)
            df.to_csv(filepath)
            
            logger.info(f"Successfully fetched data for {symbol}")
            return filepath
            
        except Exception as e:
            logger.error(f"Error fetching data for {symbol}: {str(e)}")
            raise

class DataProcessor:
    def __init__(self):
        self.processed_data_path = "/Users/usermail/Desktop/autoML/data/processed"
        os.makedirs(self.processed_data_path, exist_ok=True)
        
    def process_stock_data(self, raw_file_path: str) -> str:
        try:
            df = pd.read_csv(raw_file_path, index_col=0, parse_dates=True)
            
            # Handle missing values
            df.fillna(method='ffill', inplace=True)
            df.fillna(method='bfill', inplace=True)
            
            # Add technical indicators
            df['Returns'] = df['Close'].pct_change()
            df['SMA_20'] = df['Close'].rolling(window=20).mean()
            df['SMA_50'] = df['Close'].rolling(window=50).mean()
            df['RSI'] = self._calculate_rsi(df['Close'])
            df['Volatility'] = df['Returns'].rolling(window=20).std()
            
            # Create additional features
            df['Price_Range'] = df['High'] - df['Low']
            df['Price_Change'] = df['Close'] - df['Open']
            df['Volume_MA'] = df['Volume'].rolling(window=5).mean()
            df['Volume_Change'] = df['Volume'].pct_change()
            
            # Remove rows with NaN values
            df = df.dropna()
            
            # Save processed data
            filename = os.path.basename(raw_file_path).replace('.csv', '_processed.csv')
            processed_path = os.path.join(self.processed_data_path, filename)
            df.to_csv(processed_path)
            
            logger.info(f"Successfully processed data: {filename}")
            return processed_path
            
        except Exception as e:
            logger.error(f"Error processing data: {str(e)}")
            raise
    
    def _calculate_rsi(self, prices: pd.Series, period: int = 14) -> pd.Series:
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

class DataManager:
    def __init__(self):
        self.data_fetcher = DataFetcher()
        self.data_processor = DataProcessor()
        
    async def fetch_and_process_data(
        self,
        symbol: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> str:
        try:
            raw_file_path = await self.data_fetcher.fetch_stock_data(symbol, start_date, end_date)
            processed_file_path = self.data_processor.process_stock_data(raw_file_path)
            return processed_file_path
        except Exception as e:
            logger.error(f"Error in fetch_and_process_data: {str(e)}")
            raise