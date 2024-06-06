import time
from threading import Thread
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
from ibapi.common import OrderId


class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.nextOrderId = None

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.nextOrderId = orderId
        print(f"Next valid order ID: {self.nextOrderId}")


def create_contract(symbol: str, sec_type: str, exchange: str, currency: str) -> Contract:
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.exchange = exchange
    contract.currency = currency
    return contract


def create_order(order_type: str, quantity: int, action: str, price: float = None) -> Order:
    order = Order()
    order.orderType = order_type
    order.totalQuantity = quantity
    order.action = action
    order.eTradeOnly = ""
    order.firmQuoteOnly = ""
    if price is not None:
        order.lmtPrice = price
    return order



def create_bracket_order(parent_order_id: OrderId, quantity: int, buy_price: float, profit_price: float, stop_loss_price: float):
    parent = create_order('LMT', quantity, 'BUY', buy_price)
    parent.orderId = parent_order_id
    parent.transmit = False

    take_profit = create_order('LMT', quantity, 'SELL', profit_price)
    take_profit.orderId = parent_order_id + 1
    take_profit.parentId = parent_order_id
    take_profit.transmit = False

    stop_loss = create_order('STP', quantity, 'SELL')
    stop_loss.auxPrice = stop_loss_price
    stop_loss.orderId = parent_order_id + 2
    stop_loss.parentId = parent_order_id
    stop_loss.transmit = True

    return [parent, take_profit, stop_loss]


def main():
    app = IBApi()
    app.connect("127.0.0.1", 7496, 0)

    # Start the socket in a thread
    api_thread = Thread(target=app.run)
    api_thread.start()

    # Wait until nextOrderId is received
    while not isinstance(app.nextOrderId, int):
        print("Waiting for nextOrderId...")
        time.sleep(1)

    print(f"Received nextOrderId: {app.nextOrderId}")

    contract = create_contract("AAPL", "STK", "SMART", "USD")
    orders = create_bracket_order(app.nextOrderId, 1, 182, 210, 170)

    for order in orders:
        app.placeOrder(order.orderId, contract, order)

    # Give some time for orders to be placed
    time.sleep(5)

    app.disconnect()


if __name__ == "__main__":
    main()
