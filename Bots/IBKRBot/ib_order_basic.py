# -*- coding: utf-8 -*-
"""

"""


from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
import threading
import time


class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def error(self, reqId, errorCode, errorString):
        print("Error {} {} {}".format(reqId,errorCode,errorString))
        
    def nextValidId(self, orderId):
        super().nextValidId(orderId)
        self.nextValidOrderId = orderId
        print("NextValidId:", orderId)

def websocket_con():
    app.run()
    
app = TradingApp()
app.connect("127.0.0.1", 7496, clientId=1)

# Starting a separate daemon thread to execute the websocket connection
con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()

# Adding some latency to ensure that the connection is established
time.sleep(1)

# Creating an object of the Contract class - will be used as a parameter for other function calls
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "ISLAND"

# Creating an object of the Order class - will be used as a parameter for other function calls
order = Order()
order.action = "BUY"
order.orderType = "LMT"
order.totalQuantity = 1
order.lmtPrice = 190
order.eTradeOnly = ""
order.firmQuoteOnly = ""
# Ensure nextValidOrderId is set before placing the order
while app.nextValidOrderId is None:
    print("Waiting for nextValidOrderId...")
    time.sleep(1)

app.placeOrder(app.nextValidOrderId, contract, order)  # EClient function to place order
#app.cancelOrder(5)
time.sleep(5)  # Adding some latency to ensure that the order is placed