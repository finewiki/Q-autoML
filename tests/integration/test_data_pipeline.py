import pytest
from src.data.data_manager import FinancialDataManager
from src.data.data_processor import StockDataProcessor

class TestDataPipeline:
    @pytest.fixture
    def data_manager(self):
        return FinancialDataManager()
    
    @pytest.fixture
    def data_processor(self):
        return StockDataProcessor()
    
    def test_fetch_and_process(self, data_manager, data_processor):
        # Test complete data pipeline
        symbol = "AAPL"
        raw_data = data_manager.fetch_stock_data(symbol)
        processed_data = data_processor.process_data(raw_data)
        
        assert not processed_data.isnull().any().any()
        assert "SMA_20" in processed_data.columns
        assert "RSI" in processed_data.columns