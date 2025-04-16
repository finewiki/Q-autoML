import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

def fetch_raw_stock_data(
    symbols=['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META'],
    period='1y',
    interval='1d'
):
    """
    Fetch raw stock data and save to raw directory
    """
    raw_dir = "/Users/usermail/Desktop/autoML/data/raw"
    os.makedirs(raw_dir, exist_ok=True)
    
    for symbol in symbols:
        try:
            # Fetch data from Yahoo Finance
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period, interval=interval)
            
            # Save raw data with timestamp
            timestamp = datetime.now().strftime('%Y%m%d')
            filename = f"{symbol}_raw_{timestamp}.csv"
            filepath = os.path.join(raw_dir, filename)
            
            # Save with all original columns
            data.to_csv(filepath)
            
            print(f"Successfully fetched and saved raw data for {symbol}")
            
        except Exception as e:
            print(f"Error fetching data for {symbol}: {str(e)}")

if __name__ == "__main__":
    fetch_raw_stock_data()