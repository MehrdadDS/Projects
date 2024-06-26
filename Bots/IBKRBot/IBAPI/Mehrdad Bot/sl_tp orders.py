from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
import pandas as pd
import threading
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class IBApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.positions = []
        self.positions_df = pd.DataFrame()
        self.nextOrderId = None
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.done = False

    def position(self, account, contract, position, avgCost):
        if position != 0:
            self.positions.append({
                'account': account,
                'symbol': contract.symbol,
                'secType': contract.secType,
                'exchange': contract.exchange,
                'position': position,
                'avgCost': avgCost
            })

    def positionEnd(self):
        self.positions_df = pd.DataFrame(self.positions)
        logger.info(f"Positions DataFrame:\n{self.positions_df}")
        with self.condition:
            self.done = True
            self.condition.notify_all()

    def nextValidId(self, orderId):
        self.nextOrderId = orderId
        logger.info(f"Next Order ID: {self.nextOrderId}")
        self.reqPositions()

    def stop(self):
        self.done = True
        self.disconnect()

    def create_order(self, action, quantity, orderType, price):
        order = Order()
        order.action = action
        order.totalQuantity = quantity
        order.orderType = orderType
        if orderType == "LMT":
            order.lmtPrice = price
        elif orderType == "STP":
            order.auxPrice = price
        order.transmit = True
        order.tif = "GTC"
        return order

    def place_oco_order(self, symbol, secType, exchange, quantity, stop_price, target_price):
        contract = Contract()
        contract.symbol = symbol
        contract.secType = secType
        contract.exchange = exchange
        contract.currency = "USD"

        logger.info(f"Placing OCO orders for {symbol}")

        # Stop Loss Order
        stop_order = self.create_order("SELL", quantity, "STP", stop_price)
        stop_order.ocaGroup = f"OCA_{symbol}"
        stop_order.ocaType = 1  # 1 means cancel the remaining order if one of them fills
        stop_order.eTradeOnly = ""
        stop_order.firmQuoteOnly = ""

        # Target Profit Order
        limit_order = self.create_order("SELL", quantity, "LMT", target_price)
        limit_order.ocaGroup = f"OCA_{symbol}"
        limit_order.ocaType = 1  # 1 means cancel the remaining order if one of them fills
        limit_order.eTradeOnly = ""
        limit_order.firmQuoteOnly = ""

        logger.info(f"Stop Order: {stop_order}")
        logger.info(f"Limit Order: {limit_order}")

        self.placeOrder(self.nextOrderId, contract, stop_order)
        self.placeOrder(self.nextOrderId + 1, contract, limit_order)
        self.nextOrderId += 2

def main():
    app = IBApp()
    app.connect("127.0.0.1", 7497, 0)

    def run_loop():
        app.run()

    api_thread = threading.Thread(target=run_loop, daemon=True)
    api_thread.start()

    with app.condition:
        app.condition.wait_for(lambda: app.done)

    for index, row in app.positions_df.iterrows():
        symbol = row['symbol']
        secType = row['secType']
        exchange = "SMART"
        quantity = abs(row['position'])
        avg_cost = row['avgCost']
        stop_price = round(avg_cost * 0.8, 2)
        target_price = round(avg_cost * 1.2, 2)

        app.place_oco_order(symbol, secType, exchange, quantity, stop_price, target_price)

    app.stop()
    api_thread.join()

if __name__ == "__main__":
    main()
