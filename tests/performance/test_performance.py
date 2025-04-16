import pytest
import time
import numpy as np
from src.data.data_processor import StockDataProcessor

class TestPerformance:
    @pytest.fixture
    def large_dataset(self):
        return np.random.randn(100000, 5)
    
    def test_processing_speed(self, large_dataset):
        processor = StockDataProcessor()
        
        start_time = time.time()
        processor.process_data(large_dataset)
        end_time = time.time()
        
        processing_time = end_time - start_time
        assert processing_time < 5.0  # Should process within 5 seconds