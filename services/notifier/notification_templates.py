class NotificationTemplates:
    @staticmethod
    def model_complete_template(model_name: str, metrics: Dict) -> str:
        return f"""
        Model Training Complete
        ----------------------
        Model Name: {model_name}
        
        Performance Metrics:
        - Accuracy: {metrics.get('accuracy', 'N/A')}
        - Precision: {metrics.get('precision', 'N/A')}
        - Recall: {metrics.get('recall', 'N/A')}
        - F1 Score: {metrics.get('f1_score', 'N/A')}
        
        Training Duration: {metrics.get('training_time', 'N/A')}
        """

    @staticmethod
    def alert_template(alert_type: str, message: str) -> str:
        return f"""
        Alert: {alert_type}
        ------------------
        {message}
        
        Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """