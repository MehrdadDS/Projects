from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.utils import iswrapper
import pandas as pd
import datetime
import time
from threading import Thread

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = {}
    
    @iswrapper
    def historicalData(self, reqId, bar):
        if reqId not in self.data:
            self.data[reqId] = []
        self.data[reqId].append([bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume])
    
    @iswrapper
    def historicalDataEnd(self, reqId, start, end):
        self.disconnect()

class TradingApp:
    def __init__(self):
        self.app = IBApi()
        self.app.connect("127.0.0.1", 7496, 0)
        self.app_thread = Thread(target=self.run_loop)
        self.app_thread.start()
        time.sleep(1)  # Give the connection time to establish
    
    def run_loop(self):
        self.app.run()
    
    def fetch_historical_data(self, ticker, duration, bar_size):
        contract = Contract()
        contract.symbol = ticker
        contract.secType = "STK"
        contract.exchange = "ISLAND"
        contract.currency = "USD"
        self.app.reqHistoricalData(1, contract, "", duration, bar_size, "TRADES", 1, 1, False, [])
        time.sleep(5)  # Wait for data to be returned
        df = pd.DataFrame(self.app.data[1], columns=["Date", "Open", "High", "Low", "Close", "Volume"])
        df["Date"] = pd.to_datetime(df["Date"])
        df.insert(1,"Time Frame",bar_size)
        df.set_index("Date", inplace=True)
        return df
    
    def calculate_indicators(self, df):
        df["MA34"] = df["Close"].rolling(window=34).mean()
        df["MA131"] = df["Close"].rolling(window=131).mean()
        df["EMA12"] = df["Close"].ewm(span=12, adjust=False).mean()
        return df
    
    def check_conditions(self, df):
        if (df["Close"].iloc[-1] > df["MA34"].iloc[-1]) and (df["MA34"].iloc[-1] > df["MA131"].iloc[-1]):
            return True
        return False
    

    def swing_trader_check_conditions(self,df):
        # Check first state: Wave crosses above the Tunnel
        " When close is above High of the wave | High of Wave is above High of Tunnel "
        if (df["Close"].iloc[-1] > df["Wave_EMA_High"].iloc[-1]) and (df["Wave_EMA_High"].iloc[-1] > df["Tunnel_EMA_High"].iloc[-1]) : return True 
        
        else : return False

    def wavy_tunnel(self,df):
        # Ensure 'Close', 'High', and 'Low' columns exist
        required_columns = ['Close', 'High', 'Low']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"DataFrame must contain '{col}' column")

        # Part 1: Wave Plot
        wave_length = 34
        df['Wave_EMA_High'] = df['High'].ewm(span=wave_length, adjust=False).mean()
        df['Wave_EMA_Close'] = df['Close'].ewm(span=wave_length, adjust=False).mean()
        df['Wave_EMA_Low'] = df['Low'].ewm(span=wave_length, adjust=False).mean()

        # Part 2: Tunnel Plot
        length_tun_high = 169
        length_tun_low = 144
        df['Tunnel_EMA_High'] = df['Close'].ewm(span=length_tun_high, adjust=False).mean()
        df['Tunnel_EMA_Low'] = df['Close'].ewm(span=length_tun_low, adjust=False).mean()

        # Part 3: Filter 12 EMA
        length_filter = 12
        df['EMA_12_Filter'] = df['Close'].ewm(span=length_filter, adjust=False).mean()

        # Part 4: Action bands plot
        band_percentage = 50 / 100
        df['Band_Distance'] = df['Wave_EMA_Close'] * band_percentage
        df['Upper_Band'] = df['Wave_EMA_Close'] + df['Band_Distance']
        df['Lower_Band'] = df['Wave_EMA_Close'] - df['Band_Distance']

        # Part 5: Weekly Bands (assuming weekly data is provided in the same DataFrame for simplicity)
        # Assuming df contains weekly data under a different column for simplicity
        df['Weekly_EMA'] = df['Close'].ewm(span=wave_length, adjust=False).mean()
        df['Weekly_Upper_Band'] = df['Weekly_EMA'] + df['Band_Distance']
        df['Weekly_Lower_Band'] = df['Weekly_EMA'] - df['Band_Distance']

        # Part 6: Support Band
        support_length = 21
        df['SMA'] = df['Close'].rolling(window=support_length).mean()
        df['EMA'] = df['Close'].ewm(span=support_length, adjust=False).mean()

        # Fill the DataFrame with necessary calculations
        return df


    def run_strategy(self, tickers):
        self.db = {}
        for ticker in tickers:
            data = pd.DataFrame()
            print(f"Checking {ticker}")
            for duration, bar_size in [("30 D", "15 mins"), ("60 D", "1 hour"), ("120 D", "4 hours"), ("1 Y", "1 day"), ("2 Y", "1 week")]:
                df = self.fetch_historical_data(ticker, duration, bar_size)
                time.sleep(5)
                #df = self.calculate_indicators(df)
                #df = self.calculate_macd(df)
                df = self.wavy_tunnel(df)
                data = pd.concat([data,df])
            
            self.db[ticker] = data
            
            if bar_size == "1 hour" and self.check_conditions(df):
                print(f"Buy signal for {ticker}")
    
    def disconnect(self):
        self.app.disconnect()
        self.app_thread.join()


    # Calculate Technical Indicators
    def calculate_macd(df):
    # Ensure 'Close' column exists
        if 'Close' not in df.columns:
            raise ValueError("DataFrame must contain 'Close' column")
        # Calculate the short-term EMA (12 periods)
        short_ema = df['Close'].ewm(span=12, adjust=False).mean()
        # Calculate the long-term EMA (26 periods)
        long_ema = df['Close'].ewm(span=26, adjust=False).mean()
        # Calculate the MACD line
        macd_line = short_ema - long_ema
        # Calculate the Signal line (9 periods EMA of MACD line)
        signal_line = macd_line.ewm(span=9, adjust=False).mean()
        # Calculate the MACD Histogram
        macd_histogram = macd_line - signal_line
        
        # Add these values to the dataframe
        df['MACD_Line'] = macd_line
        df['Signal_Line'] = signal_line
        df['MACD_Histogram'] = macd_histogram     
        return df




if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]
    trading_app = TradingApp()
    trading_app.run_strategy(tickers)
    trading_app.disconnect()