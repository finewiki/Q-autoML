import pytest
import pandas as pd
import numpy as np

@pytest.fixture(scope="session")
def sample_stock_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31')
    data = pd.DataFrame({
        'Open': np.random.randn(len(dates)) + 100,
        'High': np.random.randn(len(dates)) + 102,
        'Low': np.random.randn(len(dates)) + 98,
        'Close': np.random.randn(len(dates)) + 100,
        'Volume': np.random.randint(1000000, 10000000, len(dates))
    }, index=dates)
    return data