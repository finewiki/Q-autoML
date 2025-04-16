import pytest
from src.data.data_manager import FinancialDataManager
from src.models.model_trainer import ModelTrainer
from src.evaluation.evaluator import ModelEvaluator

class TestCompleteFlow:
    @pytest.fixture
    def setup_pipeline(self):
        data_manager = FinancialDataManager()
        model_trainer = ModelTrainer()
        evaluator = ModelEvaluator()
        return data_manager, model_trainer, evaluator
    
    def test_end_to_end_flow(self, setup_pipeline):
        data_manager, model_trainer, evaluator = setup_pipeline
        
        # Fetch and process data
        data = data_manager.fetch_stock_data("AAPL")
        
        # Train model
        model = model_trainer.train(data)
        
        # Evaluate results
        metrics = evaluator.evaluate(model, data)
        
        assert metrics['accuracy'] > 0.6
        assert metrics['f1_score'] > 0.6