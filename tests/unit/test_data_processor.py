import pytest
import numpy as np
from src.data.data_processor import StockDataProcessor

class TestStockDataProcessor:
    @pytest.fixture
    def processor(self):
        return StockDataProcessor()
    
    def test_clean_data(self, processor):
        test_data = np.array([1.0, np.nan, 2.0, np.inf, 3.0])
        expected = np.array([1.0, 2.0, 3.0])
        result = processor.clean_data(test_data)
        np.testing.assert_array_equal(result, expected)
    
    def test_calculate_sma(self, processor):
        data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        window = 3
        expected = np.array([np.nan, np.nan, 2.0, 3.0, 4.0])
        result = processor.calculate_sma(data, window)
        np.testing.assert_array_almost_equal(result, expected)