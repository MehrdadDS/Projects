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
            

    def calculate_macd(self):
        # Ensure 'Close' column exists
        if 'Close' not in self.df.columns:
            raise ValueError("DataFrame must contain 'Close' column")
        # Calculate the short-term EMA (12 periods)
        short_ema = self.df['Close'].ewm(span=12, adjust=False).mean()
        # Calculate the long-term EMA (26 periods)
        long_ema = self.df['Close'].ewm(span=26, adjust=False).mean()
        # Calculate the MACD line
        macd_line = short_ema - long_ema
        # Calculate the Signal line (9 periods EMA of MACD line)
        signal_line = macd_line.ewm(span=9, adjust=False).mean()
        # Calculate the MACD Histogram
        macd_histogram = macd_line - signal_line
        
        # Add these values to the dataframe
        self.df['MACD_Line'] = macd_line
        self.df['Signal_Line'] = signal_line
        self.df['MACD_Histogram'] = macd_histogram
        return self.df
    
    def wavy_tunnel(self):
        
        # Part 1: Wave Plot
        wave_length = 34
        self.df['Wave_EMA_High'] = self.df['High'].ewm(span=wave_length, adjust=False).mean()
        self.df['Wave_EMA_Close'] = self.df['Close'].ewm(span=wave_length, adjust=False).mean()
        self.df['Wave_EMA_Low'] = self.df['Low'].ewm(span=wave_length, adjust=False).mean()

        # Part 2: Tunnel Plot
        length_tun_high = 169
        length_tun_low = 144
        self.df['Tunnel_EMA_High'] = self.df['Close'].ewm(span=length_tun_high, adjust=False).mean()
        self.df['Tunnel_EMA_Low'] = self.df['Close'].ewm(span=length_tun_low, adjust=False).mean()

        # Part 3: Filter 12 EMA
        length_filter = 12
        self.df['EMA_12_Filter'] = self.df['Close'].ewm(span=length_filter, adjust=False).mean()

        # Part 4: Action bands plot
        band_percentage = 50 / 100
        self.df['Band_Distance'] = self.df['Wave_EMA_Close'] * band_percentage
        self.df['Upper_Band'] = self.df['Wave_EMA_Close'] + self.df['Band_Distance']
        self.df['Lower_Band'] = self.df['Wave_EMA_Close'] - self.df['Band_Distance']

        # Part 5: Weekly Bands (assuming weekly data is provided in the same DataFrame for simplicity)
        # Assuming df contains weekly data under a different column for simplicity
        self.df['Weekly_EMA'] = self.df['Close'].ewm(span=wave_length, adjust=False).mean()
        self.df['Weekly_Upper_Band'] = self.df['Weekly_EMA'] + self.df['Band_Distance']
        self.df['Weekly_Lower_Band'] = self.df['Weekly_EMA'] - self.df['Band_Distance']

        # Part 6: Support Band
        support_length = 21
        self.df['SMA'] = self.df['Close'].rolling(window=support_length).mean()
        self.df['EMA'] = self.df['Close'].ewm(span=support_length, adjust=False).mean()

        # Fill the DataFrame with necessary calculations
        return self.df
    


        def ichimoku(self):
        high_9 = self.df['High'].rolling(window=9).max()
        low_9 = self.df['Low'].rolling(window=9).min()
        self.df['Tenkan_sen'] = (high_9 + low_9) / 2

        high_26 = self.df['High'].rolling(window=26).max()
        low_26 = self.df['Low'].rolling(window=26).min()
        self.df['Kijun_sen'] = (high_26 + low_26) / 2

        self.df['Senkou_Span_A'] = ((self.df['Tenkan_sen'] + self.df['Kijun_sen']) / 2).shift(26)

        high_52 = self.df['High'].rolling(window=52).max()
        low_52 = self.df['Low'].rolling(window=52).min()
        self.df['Senkou_Span_B'] = ((high_52 + low_52) / 2).shift(26)

        self.df['Chikou_Span'] = self.df['Close'].shift(-26)

        return self.df