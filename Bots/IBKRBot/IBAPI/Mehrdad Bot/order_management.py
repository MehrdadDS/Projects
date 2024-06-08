# order_management.py

from ibapi.order import Order
import time
from ibapi.contract import Contract
import numpy as np
import pandas as pd

class OrderManager:
    def __init__(self, app, max_amount):
        self.app = app
        self.max_amount = max_amount
        self.orders = []

    def create_bracket_order(self, order_id, action, quantity, limit_price, take_profit_limit_price, stop_loss_price):
        parent_order = Order()
        parent_order.orderId = order_id
        parent_order.action = action
        parent_order.orderType = "LMT"
        parent_order.totalQuantity = quantity
        parent_order.lmtPrice = limit_price
        parent_order.transmit = False
        parent_order.eTradeOnly=""
        parent_order.firmQuoteOnly = ""        

        take_profit = Order()
        take_profit.orderId = order_id + 1
        take_profit.action = "SELL" if action == "BUY" else "BUY"
        take_profit.orderType = "LMT"
        take_profit.totalQuantity = quantity
        take_profit.lmtPrice = take_profit_limit_price
        take_profit.parentId = order_id
        take_profit.transmit = True
        take_profit.eTradeOnly=""
        take_profit.firmQuoteOnly = ""


        stop_loss = Order()
        stop_loss.orderId = order_id + 2
        stop_loss.action = "SELL" if action == "BUY" else "BUY"
        stop_loss.orderType = "STP"
        stop_loss.auxPrice = stop_loss_price
        stop_loss.totalQuantity = quantity
        stop_loss.parentId = order_id
        stop_loss.transmit = True
        stop_loss.eTradeOnly=""
        stop_loss.firmQuoteOnly = ""
        

        bracket_order = [parent_order, take_profit, stop_loss]
        return bracket_order

    def process_signals(self, signals_df):
        for index, signal in signals_df.iterrows():
            if signal['trade_trigger'] == 'Yes':
                #quantity = self.calculate_quantity(signal['entry_point'])
                quantity = 300
                order_id = self.app.nextOrderId
                action = "BUY"  # Assuming a long position for simplicity
                limit_price = signal['entry_point'] -10
                take_profit_limit_price = signal['target']
                stop_loss_price = signal['stoploss']
                
                bracket_order = self.create_bracket_order(order_id, action, quantity, limit_price, take_profit_limit_price, stop_loss_price)
                for order in bracket_order:
                    self.app.placeOrder(order.orderId, self.create_contract(signal['ticker']), order)
                    self.orders.append({
                        "time_placement": time.time(),
                        "buying_price": limit_price,
                        "stop_loss": stop_loss_price,
                        "profit_price": take_profit_limit_price,
                        "order_id": order.orderId,
                        "ticker": signal['ticker'],
                        "executed": False,
                        "time_frame": signal['time_frame'],
                        "risk_to_reward": signal['risk_to_reward']
                    })
                    time.sleep(1)  # To ensure the order is placed

    def calculate_quantity(self, entry_price):
        return round(self.max_amount / entry_price, 2)

    def create_contract(self, ticker):
        contract = Contract()
        contract.symbol = ticker
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        return contract


    def open_orders(self):
        self.app.reqAllOpenOrders()
        time.sleep(2)  # Wait for open orders to be received
        open_orders_df = pd.DataFrame(self.app.open_orders, columns=[
            'time_of_placing_order', 'ticker', 'type', 'action', 'quantity', 'entry_point', 
            'stop_loss', 'filled_quantity', 'target_price'
        ])
        return open_orders_df