from ibapi.contract import Contract
from ibapi.order import Order
import pandas as pd
from telegrambot import TelegramBot

class OrderManager(Contract,Order):
    def __init__(self, api_client, initial_balance: float):
        self.api_client = api_client
        self.balance = initial_balance
        #self.api_client.connect("127.0.0.1", 7496, 0)
        self.api_client.nextOrderId = None
        self.api_client.reqIds(-1)

    def place_buy_stop_limit_order(self, ticker, entry_point, stoploss, quantity):
        if entry_point * quantity > self.balance:
            print(f"Not enough balance to place order for {ticker}")
            return

        contract = Contract()
        contract.symbol = ticker
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"

        order = Order()
        order.action = "BUY"
        order.orderType = "STP LMT"
        order.totalQuantity = quantity
        order.lmtPrice = entry_point
        order.auxPrice = stoploss
        order.eTradeOnly = ""
        order.firmQuoteOnly = ""

        self.api_client.placeOrder(self.api_client.nextOrderId, contract, order)
        print(f"Placed order for {ticker} with entry point {entry_point} and stoploss {stoploss}")
        TelegramBot.tlg_send_message(f"{self.api_client.nextOrderId}) Buy order: {ticker}\n- entry point:@{entry_point}\n- stoploss:@{stoploss}")
        self.api_client.nextOrderId +=1

        self.balance -= entry_point * quantity

    def process_signals(self, signals_df: pd.DataFrame):
        for _, row in signals_df.iterrows():
            if row['trade_trigger'] == 'Yes':
                ticker = row['ticker']
                entry_point = row['entry_point']
                stoploss = row['stoploss']
                target = row['target']
                time_frame = row['time_frame']

                # Assuming a quantity of 100 for simplicity
                quantity = 1

                self.place_buy_stop_limit_order(ticker, entry_point, stoploss, quantity)
