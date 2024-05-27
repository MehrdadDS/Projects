from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.utils import iswrapper
import pandas as pd
import datetime
import time
from threading import Thread
from indicators import TechnicalIndicators

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
        df.insert(1,"Ticker",ticker)
        df.set_index("Date", inplace=True)
        return df
    
    
    def create_historical_database(self, tickers):
        self.db = {}
        for ticker in tickers:
            data = pd.DataFrame()
            print(f"Checking {ticker}")
            for duration, bar_size in [("30 D", "15 mins"), ("60 D", "1 hour"), ("90 D", "4 hours"), ("1 Y", "1 day"), ("2 Y", "1 week")]:
                df = self.fetch_historical_data(ticker, duration, bar_size)
                time.sleep(5)

                
                # Initialize the TechnicalIndicators class with the dataframe
                df_for_TA = TechnicalIndicators(df)
                df = df_for_TA.calculate_macd()
                df = df_for_TA.wavy_tunnel()
                df = df_for_TA.ichimoku()

                data = pd.concat([data,df])
            
            self.db[ticker] = data
        return self.db
    
    def disconnect(self):
        self.app.disconnect()
        self.app_thread.join()





if __name__ == "__main__":
    tickers = ["AAPL", "TSLA"]
    trading_app = TradingApp()
    trading_app.create_historical_database(tickers)
    trading_app.disconnect()