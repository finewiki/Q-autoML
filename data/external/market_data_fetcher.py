import pandas as pd
import requests
import os
from datetime import datetime
from typing import Dict, Optional

class MarketDataFetcher:
    def __init__(self):
        self.external_dir = "/Users/usermail/Desktop/autoML/data/external"
        os.makedirs(self.external_dir, exist_ok=True)
        
    def fetch_market_indices(self) -> pd.DataFrame:
        """Fetch major market indices data"""
        indices = ['^GSPC', '^DJI', '^IXIC', '^FTSE']  # S&P 500, Dow Jones, NASDAQ, FTSE
        dfs = []
        
        for index in indices:
            try:
                df = yf.download(index, period='1y')
                df['Index'] = index
                dfs.append(df)
            except Exception as e:
                print(f"Error fetching {index}: {e}")
                
        combined_df = pd.concat(dfs)
        self._save_data(combined_df, 'market_indices.csv')
        return combined_df
    
    def fetch_economic_indicators(self) -> pd.DataFrame:
        """Fetch economic indicators from FRED"""
        indicators = {
            'GDP': 'GDP',
            'Inflation': 'CPIAUCSL',
            'Unemployment': 'UNRATE',
            'FedRate': 'FEDFUNDS'
        }
        
        # Placeholder for actual API implementation
        data = {'Date': [], 'Indicator': [], 'Value': []}
        self._save_data(pd.DataFrame(data), 'economic_indicators.csv')
        return pd.DataFrame(data)
    
    def fetch_sector_performance(self) -> pd.DataFrame:
        """Fetch sector ETF performance"""
        sector_etfs = {
            'Technology': 'XLK',
            'Financial': 'XLF',
            'Healthcare': 'XLV',
            'Energy': 'XLE'
        }
        
        dfs = []
        for sector, symbol in sector_etfs.items():
            try:
                df = yf.download(symbol, period='1y')
                df['Sector'] = sector
                dfs.append(df)
            except Exception as e:
                print(f"Error fetching {sector}: {e}")
                
        combined_df = pd.concat(dfs)
        self._save_data(combined_df, 'sector_performance.csv')
        return combined_df
    
    def _save_data(self, df: pd.DataFrame, filename: str):
        """Save external data with timestamp"""
        timestamp = datetime.now().strftime('%Y%m%d')
        filepath = os.path.join(self.external_dir, f"{timestamp}_{filename}")
        df.to_csv(filepath)

if __name__ == "__main__":
    fetcher = MarketDataFetcher()
    fetcher.fetch_market_indices()
    fetcher.fetch_economic_indicators()
    fetcher.fetch_sector_performance()