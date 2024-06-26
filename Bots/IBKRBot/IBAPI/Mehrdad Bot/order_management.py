# order_management.py

from ibapi.order import Order
import time
from ibapi.contract import Contract
import numpy as np
import pandas as pd
from datetime import datetime


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
        parent_order.totalQuantity = int(quantity)
        parent_order.lmtPrice = limit_price
        parent_order.transmit = False
        parent_order.eTradeOnly=""
        parent_order.firmQuoteOnly = ""        

        take_profit = Order()
        take_profit.orderId = order_id + 1
        take_profit.action = "SELL" if action == "BUY" else "BUY"
        take_profit.orderType = "LMT"
        take_profit.totalQuantity = int(quantity)
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
        stop_loss.totalQuantity = int(quantity)
        stop_loss.parentId = order_id
        stop_loss.transmit = True
        stop_loss.eTradeOnly=""
        stop_loss.firmQuoteOnly = ""
        

        bracket_order = [parent_order, take_profit, stop_loss]
        return bracket_order

    def process_signals(self, signals_df):
        for index, signal in signals_df.iterrows():
            if signal['trade_trigger'] == 'Yes':
                quantity = self.calculate_quantity(signal['entry_point'])
                #quantity = 300
                order_id = self.app.nextOrderId
                action = "BUY"  # Assuming a long position for simplicity
                limit_price = signal['entry_point']
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
                        "risk_to_reward": signal['risk_to_reward'],
                        "potential_profit":signal['potential_profit'],
                        "potential_loss":signal['potential_loss'],
                    })
                    time.sleep(5)  # To ensure the order is placed

    def calculate_quantity(self, entry_price):
        return int(self.max_amount // entry_price)

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
            'order_id', 'ticker', 'type', 'action', 'quantity', 'entry_point', 
            'stop_loss', 'filled_quantity', 'target_price', 'order_state', 'tif'#, 'time_placement'#, 'status_history'
        ])
        return open_orders_df
    

    def placing_selling_OCA_orders(self, positions_df, sell_limit_price, stop_loss_price):
        open_orders_df = self.open_orders()

        for index, position in positions_df.iterrows():
            ticker = position['Symbol']
            position_quantity = position['Position']

            # Check if there are existing sell limit or stop loss orders for this ticker
            existing_orders = open_orders_df[open_orders_df['ticker'] == ticker]
            has_sell_limit = not existing_orders[(existing_orders['type'] == 'LMT') & (existing_orders['action'] == 'SELL')].empty
            has_stop_loss = not existing_orders[(existing_orders['type'] == 'STP') & (existing_orders['action'] == 'SELL')].empty

            if not has_sell_limit or not has_stop_loss:
                order_id = self.app.nextOrderId
                sell_limit_order = Order()
                sell_limit_order.orderId = order_id
                sell_limit_order.action = "SELL"
                sell_limit_order.orderType = "LMT"
                sell_limit_order.totalQuantity = position_quantity
                sell_limit_order.lmtPrice = round(sell_limit_price,1)
                sell_limit_order.tif = "GTC"
                sell_limit_order.ocaGroup = f"OCA_{ticker}_{order_id}"
                sell_limit_order.eTradeOnly=""
                sell_limit_order.firmQuoteOnly = ""


                stop_loss_order = Order()
                stop_loss_order.orderId = order_id + 1
                stop_loss_order.action = "SELL"
                stop_loss_order.orderType = "STP"
                stop_loss_order.totalQuantity = position_quantity
                stop_loss_order.auxPrice = round(stop_loss_price,1)
                stop_loss_order.tif = "GTC"
                stop_loss_order.ocaGroup = f"OCA_{ticker}_{order_id}"
                stop_loss_order.eTradeOnly=""
                stop_loss_order.firmQuoteOnly = ""


                contract = self.create_contract(ticker)
                self.app.placeOrder(sell_limit_order.orderId, contract, sell_limit_order)
                time.sleep(5)
                self.app.placeOrder(stop_loss_order.orderId, contract, stop_loss_order)
                time.sleep(5)

                self.orders.append({
                    #"time_placement": datetime.now(),
                    "ticker": ticker,
                    "type": sell_limit_order.orderType,
                    "action": sell_limit_order.action,
                    "quantity": position_quantity,
                    "entry_point": sell_limit_price,
                    "stop_loss": stop_loss_price,
                    "filled_quantity": 0,  # Placeholder for actual filled quantity
                    "target_price": sell_limit_price,
                    "order_id": sell_limit_order.orderId,
                    "tif": sell_limit_order.tif,
                    "oca_group": sell_limit_order.ocaGroup
                })
                self.orders.append({
                    #"time_placement": datetime.now(),
                    "ticker": ticker,
                    "type": stop_loss_order.orderType,
                    "action": stop_loss_order.action,
                    "quantity": position_quantity,
                    "entry_point": sell_limit_price,
                    "stop_loss": stop_loss_price,
                    "filled_quantity": 0,  # Placeholder for actual filled quantity
                    "target_price": sell_limit_price,
                    "order_id": stop_loss_order.orderId,
                    "tif": stop_loss_order.tif,
                    "oca_group": stop_loss_order.ocaGroup
                })
                time.sleep(1)  # To ensure the order is placed


