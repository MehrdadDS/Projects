import pandas as pd

class TechnicalIndicators:
    def __init__(self, df):
        self.df = df
        self._validate_dataframe()

    def _validate_dataframe(self):
        required_columns = ['Close', 'High', 'Low']
        for col in required_columns:
            if col not in self.df.columns:
                raise ValueError(f"DataFrame must contain '{col}' column")
            

            