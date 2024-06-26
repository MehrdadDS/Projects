# main.py

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.utils import iswrapper
import pandas as pd
import datetime
import time
from threading import Thread
from indicators import TechnicalIndicators
from Strategeies import TradingStrategies
from order_management import OrderManager
from positions import Positions
from telegrambot import TelegramBot
from ibapi.order import Order
from datetime import datetime
import sqlite3
import config
import warnings
warnings.filterwarnings("ignore")
import sql


class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = {}
        self.positions = []
        self.open_orders = []
        self.nextOrderId = None
        self.reqId = 0  # Initialize reqId


    def nextValidId(self, orderId):
        self.nextOrderId = orderId
        print("Next valid order id: ", orderId)

    def error(self, reqId, errorCode, errorString):
        print(f"Error: {reqId}, {errorCode}, {errorString}")

    def position(self, account, contract, position, avgCost):
        self.positions.append({
            "Account": account,
            "Symbol": contract.symbol,
            "SecType": contract.secType,
            "Currency": contract.currency,
            "Position": position,
            "AvgCost": avgCost
        })
        
    def positionEnd(self):
        print("PositionEnd")
        self.disconnect()

    @iswrapper
    def historicalData(self, reqId, bar):
        if reqId not in self.data:
            self.data[reqId] = []
        self.data[reqId].append([bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume])
            #self.data[reqId].append({"Date":bar.date,"Open":bar.open,"High":bar.high,"Low":bar.low,"Close":bar.close,"Volume":bar.volume})

    @iswrapper
    def openOrder(self, orderId, contract, order, orderState):
        self.open_orders.append({
            'order_id': orderId,
            'ticker': contract.symbol,
            'type': order.orderType,
            'action': order.action,
            'quantity': int(order.totalQuantity),
            'entry_point': order.lmtPrice,
            'stop_loss': order.auxPrice if order.orderType == "STP" else None,
            'filled_quantity': order.filledQuantity,
            'target_price': order.lmtPrice if order.orderType == "LMT" else None,
            'order_state': orderState.status,
            'tif': order.tif,  # Time in force
            'status_history': [],  # Initialize status history list
            'time_placement': datetime.now()  # Capture current time
        })

    @iswrapper
    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId,
                    parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
        for order in self.open_orders:
            if order['order_id'] == orderId:
                order['status_history'].append({
                    'timestamp': datetime.now(),
                    'status': status,
                    'filled': filled,
                    'remaining': remaining,
                    'avg_fill_price': avgFillPrice,
                    'last_fill_price': lastFillPrice,
                })

    @iswrapper
    def openOrderEnd(self):
        print("OpenOrderEnd")

    @iswrapper
    def historicalDataEnd(self, reqId, start, end):
        print(f"HistoricalDataEnd. ReqId: {reqId}, from {start} to {end}")

    @iswrapper
    def connectionClosed(self):
        print("Connection closed")
        self.connected = False

    @iswrapper
    def connectAck(self):
        print("Connection acknowledged")
        self.connected = True
"""I changed this part
        if reqId not in self.data:
            self.data[reqId] = []
        self.data[reqId].append([bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume])"""


class TradingApp:
    def __init__(self):
        self.app = IBApi()
        self.app.connect("127.0.0.1", 7497, 1)
        self.app_thread = Thread(target=self.run_loop)
        self.app_thread.start()
        time.sleep(1)  # Give the connection time to establish

    def run_loop(self):
        self.app.run()

    def fetch_historical_data(self,ticker, duration, bar_size):

        #endDateTime = datetime.now().strftime("%Y%m%d %H:%M:%S")
        self.app.reqId += 1
        reqId = self.app.reqId
        df = []
        contract = Contract()
        contract.symbol = ticker
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        self.app.reqHistoricalData(
                                    reqId=reqId,
                                    contract = contract,
                                    endDateTime = "",
                                    durationStr = duration,
                                    barSizeSetting = bar_size,
                                    whatToShow = "TRADES",
                                    useRTH = 1,
                                    formatDate = 1,
                                    keepUpToDate = False,
                                    chartOptions = [])
        
        time.sleep(3)  # Wait for data to be returned

#-------------
        print(f"Fetching data for reqId {reqId} and ticker {ticker}")
        if reqId in self.app.data:
            df = pd.DataFrame(self.app.data[reqId], columns=["Date", "Open", "High", "Low", "Close", "Volume"])
            df["Date"] = pd.to_datetime(df["Date"])
            df.set_index("Date", inplace=True)



            df = pd.DataFrame(self.app.data[reqId], columns=["Date", "Open", "High", "Low", "Close", "Volume"])
            df["Date"] = pd.to_datetime(df["Date"])
            df.insert(1, "Time Frame", bar_size)
            df.insert(1, "Ticker", ticker)
            df.set_index("Date", inplace=True)
            return df
        else:
            print(f"No data received for reqId {reqId}")

    def create_historical_database(self, tickers):
        self.db = {}
        for n,ticker in enumerate(tickers):
            data = pd.DataFrame()
            print(f"Pulling {ticker} data")
            i=1
            for duration, bar_size in [("5 D", "5 mins"), ("2 W", "15 mins"), ("2 M", "1 hour"), ("5 M", "4 hours"), ("1 Y", "1 day"), ("5 Y", "1 week"), ("20 Y", "1 month")]:
                ##req_id = (n-1)+i
                #i +=1
                #df =[]
                #df = self.fetch_historical_data(req_id,ticker, duration, bar_size)
                df = self.fetch_historical_data(ticker, duration, bar_size)
                time.sleep(5)
                if df is None:
                    print(f"No data for ticker {ticker} with reqId {self.app.reqId}")
                    continue
                # Initialize the TechnicalIndicators class with the dataframe
                df_for_TA = TechnicalIndicators(df)
                #df = df_for_TA.calculate_macd()
                df = df_for_TA.wavy_tunnel()
                #df = df_for_TA.ichimoku()

                data = pd.concat([data, df])
            
            self.db[ticker] = data
        return self.db

    def disconnect(self):
        self.app.disconnect()
        self.app_thread.join()

class Trader:
    def __init__(self, tickers, max_amount):
        self.tickers = tickers
        self.trading_app = TradingApp()
        self.telegram_bot = TelegramBot()
        self.order_manager = OrderManager(self.trading_app.app, max_amount)
        self.positions_manager = Positions(self.trading_app.app)
        self.signals = {}

    def generate_signals(self):
        stocks_historical_data = self.trading_app.create_historical_database(self.tickers)
        time_frames = ['5 mins', '15 mins', '1 hour', '4 hours', '1 day', '1 week']
        #time_frames = ['1 month']
        
        combined_df = pd.concat(stocks_historical_data.values())
        combined_df.to_csv('stocks_historical_data.csv')

        for ticker in stocks_historical_data.keys():
            ticker_data = stocks_historical_data[ticker]
            for tf in time_frames:
                strategy = TradingStrategies(ticker_data)
                result = strategy.wavy_tunnel_conservative_strategy(tf)
                if result:
                    if result['trade_trigger'] == "Yes":
                        self.signals[len(self.signals) + 1] = result
                        formatted_message = self.telegram_bot.format_signal(result)
                        self.telegram_bot.tlg_send_message(formatted_message)
                
                """
                result = strategy.wavy_tunnel_conservative_strategy(tf)
                result_short  = strategy.short_wavy_tunnel_conservative_strategy(tf)

                elif result_short['trade_trigger'] == "Yes":
                    self.signals[len(self.signals) + 1] = result_short
                    formatted_message = self.telegram_bot.format_signal(result_short)
                    self.telegram_bot.tlg_send_message(formatted_message)
                """
        self.signals_df = pd.DataFrame.from_dict(self.signals, orient='index')
        print(self.signals_df)
        #formatted_message = self.telegram_bot.format_signal(self.signals_df.head())
        #self.telegram_bot.tlg_send_message(formatted_message)

    def place_orders(self):
        self.order_manager.process_signals(self.signals_df)

    def check_positions(self):
        positions_df = self.positions_manager.get_positions_df()
        print(positions_df)
        self.telegram_bot.tlg_send_message(f"Current Positions:\n{positions_df.to_string()}")
        return positions_df
    
    
    def get_open_orders(self):
        open_orders_dataframe = []
        open_orders_dataframe = self.order_manager.open_orders().drop_duplicates()
        print(open_orders_dataframe)
        #self.telegram_bot.tlg_send_message(f"Open Orders:\n{open_orders_df.to_string()}")
        return open_orders_dataframe
    
    def place_selling_oca_orders(self,positions_df,sell_limit_price, stop_loss_price):
        #positions_df = self.positions_manager.get_positions_df()
        #positions_df = self.check_positions()
        self.order_manager.placing_selling_OCA_orders(positions_df, sell_limit_price, stop_loss_price)


    def run(self):
        #open_orders_df = self.get_open_orders()
        self.generate_signals()
        self.place_orders()
        positions_df = self.check_positions()
        #trader.place_selling_oca_orders(positions_df,sell_limit_price=150, stop_loss_price=130)
        self.trading_app.disconnect()

if __name__ == "__main__":
    tickers = config.medium_cap_tickers_between_50_to_100[:4]

    #tickers = ['TESS', 'TEX', 'TF', 'TFSL', 'TFX', 'TG', 'TGA', 'TGB', 'TGH', 'TGHI']
    max_amount = 10000

    trader = Trader(tickers, max_amount)
    #i = 0
    #while i<2:
    #    print(i,int(time.time()))
    trader.run()
    
    #    i +=1
    #print(time.sleep(90))
    
