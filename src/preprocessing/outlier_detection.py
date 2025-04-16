import numpy as np
import pandas as pd
from typing import List, Optional, Tuple

class OutlierDetector:
    def __init__(self, method: str = 'iqr', contamination: float = 0.1):
        self.method = method
        self.contamination = contamination
        self.boundaries = {}
        
    def fit(self, df: pd.DataFrame, columns: Optional[List[str]] = None):
        """
        Calculate boundaries for outlier detection
        """
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns
            
        for col in columns:
            if self.method == 'iqr':
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                self.boundaries[col] = (lower_bound, upper_bound)
                
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove or cap outliers based on calculated boundaries
        """
        df_clean = df.copy()
        
        for col, (lower, upper) in self.boundaries.items():
            # Cap the values instead of removing
            df_clean[col] = df_clean[col].clip(lower=lower, upper=upper)
            
        return df_clean