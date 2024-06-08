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


class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = {}
        self.positions = []
        self.open_orders = []
        self.nextOrderId = None

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
            self.data[reqId] = pd.DataFrame([{"Date":bar.date,"Open":bar.open,"High":bar.high,"Low":bar.low,"Close":bar.close,"Volume":bar.volume}])
        else:
            self.data[reqId] = pd.concat((self.data[reqId],pd.DataFrame([{"Date":bar.date,"Open":bar.open,"High":bar.high,"Low":bar.low,"Close":bar.close,"Volume":bar.volume}])))
            #self.data[reqId].append({"Date":bar.date,"Open":bar.open,"High":bar.high,"Low":bar.low,"Close":bar.close,"Volume":bar.volume})

    @iswrapper
    def openOrder(self, orderId, contract, order, orderState):
        self.open_orders.append({
            'time_of_placing_order': datetime.now(),
            'ticker': contract.symbol,
            'type': order.orderType,
            'action': order.action,
            'quantity': order.totalQuantity,
            'entry_point': order.lmtPrice,
            'stop_loss': order.auxPrice if order.orderType == "STP" else None,
            'filled_quantity': order.filledQuantity,
            'target_price': order.lmtPrice if order.orderType == "LMT" else None
        })


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

    def fetch_historical_data(self,req_id, ticker, duration, bar_size):

        #endDateTime = datetime.now().strftime("%Y%m%d %H:%M:%S")
        df = []
        contract = Contract()
        contract.symbol = ticker
        contract.secType = "STK"
        contract.exchange = "ISLAND"
        contract.currency = "USD"
        self.app.reqHistoricalData(
                                    reqId=req_id,
                                    contract = contract,
                                    endDateTime = "",
                                    durationStr = duration,
                                    barSizeSetting = bar_size,
                                    whatToShow = "TRADES",
                                    useRTH = 1,
                                    formatDate = 1,
                                    keepUpToDate = False,
                                    chartOptions = [])
        
        time.sleep(1)  # Wait for data to be returned
        df = pd.DataFrame(self.app.data[req_id], columns=["Date", "Open", "High", "Low", "Close", "Volume"])
        df["Date"] = pd.to_datetime(df["Date"])
        df.insert(1, "Time Frame", bar_size)
        df.insert(1, "Ticker", ticker)
        df.set_index("Date", inplace=True)
        return df

    def create_historical_database(self, tickers):
        self.db = {}
        for n,ticker in enumerate(tickers):
            data = pd.DataFrame()
            print(f"Pulling {ticker} data")
            i=1
            for duration, bar_size in [("5 D", "5 mins"), ("2 W", "15 mins"), ("9 W", "1 hour"), ("5 M", "4 hours"), ("1 Y", "1 day"), ("5 Y", "1 week"), ("20 Y", "1 month")]:
                req_id = (n-1)+i
                i +=1
                df =[]
                df = self.fetch_historical_data(req_id,ticker, duration, bar_size)
                time.sleep(5)

                # Initialize the TechnicalIndicators class with the dataframe
                df_for_TA = TechnicalIndicators(df)
                df = df_for_TA.calculate_macd()
                df = df_for_TA.wavy_tunnel()
                df = df_for_TA.ichimoku()

                data = pd.concat([data, df])
            
            self.db[ticker] = data
        return self.db

    def disconnect(self):
        self.app.disconnect()
        self.app_thread.join()

class Trader:
    def __init__(self, tickers, bot_token, chat_id, max_amount):
        self.tickers = tickers
        self.trading_app = TradingApp()
        self.telegram_bot = TelegramBot(bot_token, chat_id)
        self.order_manager = OrderManager(self.trading_app.app, max_amount)
        self.positions_manager = Positions(self.trading_app.app)
        self.signals = {}

    def generate_signals(self):
        stocks_historical_data = self.trading_app.create_historical_database(self.tickers)
        time_frames = ['5 mins', '15 mins', '1 hour', '4 hours', '1 day', '1 week']
        
        combined_df = pd.concat(stocks_historical_data.values())
        combined_df.to_csv('stocks_historical_data.csv')

        for ticker in stocks_historical_data.keys():
            ticker_data = stocks_historical_data[ticker]
            for tf in time_frames:
                strategy = TradingStrategies(ticker_data)
                result = strategy.wavy_tunnel_conservative_strategy(tf)
                if result['trade_trigger'] == "Yes":
                    self.signals[len(self.signals) + 1] = result
                    formatted_message = self.telegram_bot.format_signal(result)
                    self.telegram_bot.tlg_send_message(formatted_message)    

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
    
    
    def get_open_orders(self):
        open_orders_df = self.order_manager.open_orders()
        print(open_orders_df)
        self.telegram_bot.tlg_send_message(f"Open Orders:\n{open_orders_df.to_string()}")
        return open_orders_df
    
    
    def run(self):
        open_orders_df = self.get_open_orders()
        print(f"open orders:\n{open_orders_df}")
        self.generate_signals()
        self.place_orders()
        self.check_positions()
        self.trading_app.disconnect()

if __name__ == "__main__":
    tickers = ["ICLN","PYPL"]#["NIO","ICLN","SHOP","GME","PYPL","TSLA","UPST","DLTR","BYD","ATOM","MCS","ABNB","SNOW"]  # Add more tickers if needed
    bot_token = "6973724292:AAH4XTP3y1a-6EKi0yFBcqfSR45TsznSMJI"  # Replace with your actual Telegram bot token
    chat_id = "83167574"  # Replace with your actual Telegram chat ID
    max_amount = 10000

    trader = Trader(tickers, bot_token, chat_id, max_amount)
    i = 0
    while i<2:
        time.time
        trader.run()
        i +=1
        time.sleep(30)
    
