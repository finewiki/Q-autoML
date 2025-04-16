import pandas as pd
import numpy as np
from typing import Dict, Optional

class FinancialImputer:
    def __init__(self, numeric_strategy: str = 'median', 
                 categorical_strategy: str = 'mode'):
        self.numeric_strategy = numeric_strategy
        self.categorical_strategy = categorical_strategy
        self.fill_values = {}
        
    def fit(self, df: pd.DataFrame):
        """
        Calculate imputation values for each column
        """
        for column in df.columns:
            if pd.api.types.is_numeric_dtype(df[column]):
                if self.numeric_strategy == 'median':
                    self.fill_values[column] = df[column].median()
                elif self.numeric_strategy == 'mean':
                    self.fill_values[column] = df[column].mean()
            else:
                if self.categorical_strategy == 'mode':
                    self.fill_values[column] = df[column].mode()[0]
                    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply imputation to the dataset
        """
        df_imputed = df.copy()
        
        for column, fill_value in self.fill_values.items():
            df_imputed[column].fillna(fill_value, inplace=True)
            
        return df_imputed