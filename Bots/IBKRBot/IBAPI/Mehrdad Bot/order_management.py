from ibapi.contract import Contract
from ibapi.order import Order
import pandas as pd
from telegrambot import TelegramBot

class OrderManager(Contract,Order):
    def __init__(self, api_client, initial_balance: float):
        self.api_client = api_client
        self.balance = initial_balance
        #self.api_client.connect("127.0.0.1", 7496, 0)
        #self.api_client.nextOrderId = None
        self.api_client.reqIds(-1)
        


    def place_buy_limit_order(self, ticker, entry_point, stoploss, quantity,target,time_frame):
        self.order_specification ={}
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
        #order.orderType = "STP LMT"
        order.orderType = "LMT"
        order.totalQuantity = quantity
        order.lmtPrice = entry_point
        #order.auxPrice = stoploss
        order.eTradeOnly = ""
        order.firmQuoteOnly = ""
        self.order_specification[self.api_client.nextOrderId]={'ticker':ticker,'action':order.action,'order_type':order.orderType,'quantity':quantity,'entry_point':entry_point,'stop_loss':stoploss,'target':target,'time_frame':time_frame}
        self.api_client.placeOrder(self.api_client.nextOrderId, contract, order)
        print(f"Placed order for {ticker} with entry point {entry_point} and stoploss {stoploss}")
        TelegramBot.tlg_send_message(f"{self.api_client.nextOrderId}) Buy order: {ticker}\n- entry point:@{entry_point}\n- stoploss:@{stoploss}\- signal came from {time_frame}chart")
        
        self.api_client.nextOrderId +=1

        self.balance -= entry_point * quantity
        return pd.DataFrame.from_dict(self.order_specification,orient='index')

    def create_contract(symbol: str, sec_type: str, exchange: str, currency: str) -> Contract:
        contract = Contract()
        contract.symbol = symbol
        contract.secType = sec_type
        contract.exchange = exchange
        contract.currency = currency
        return contract



    def process_signals(self, signals_df: pd.DataFrame):
        self.order_tables=pd.DataFrame()
        for _, row in signals_df.iterrows():
            if row['trade_trigger'] == 'Yes':
                ticker = row['ticker']
                buy_price = row['entry_point']
                stop_loss_price = row['stoploss']
                profit_price = row['target']
                time_frame = row['time_frame']

                # Assuming a quantity of 100 for simplicity
                quantity = 1

                #t= self.place_buy_stop_limit_order(ticker, entry_point, stoploss, quantity,target,time_frame)
                parent_order_id = self.api_client.nextOrderId
                orders = self.create_bracket_order(parent_order_id, quantity, buy_price, profit_price, stop_loss_price)
                #self.order_tables = pd.concat([self.order_tables,t])
        for order in orders:
            app.placeOrder(order.orderId, contract, order)
        #return self.order_tables
    
    def create_bracket_order(self, parent_order_id: int, quantity: int, buy_price: float, profit_price: float, stop_loss_price: float):
        parent = self.create_order('LMT', quantity, 'BUY', buy_price)
        parent.orderId = parent_order_id
        parent.transmit = False

        take_profit = self.create_order('LMT', quantity, 'SELL', profit_price)
        take_profit.orderId = parent_order_id + 1
        take_profit.parentId = parent_order_id
        take_profit.transmit = False

        stop_loss = self.create_order('STP', quantity, 'SELL')
        stop_loss.auxPrice = stop_loss_price
        stop_loss.orderId = parent_order_id + 2
        stop_loss.parentId = parent_order_id
        stop_loss.transmit = True

        return [parent, take_profit, stop_loss]


    def create_order(self, order_type: str, quantity: int, action: str, price: float = None) -> Order:
        order = Order()
        order.orderType = order_type
        order.totalQuantity = quantity
        order.action = action
        order.eTradeOnly = ""
        order.firmQuoteOnly = ""
        if price is not None:
            order.lmtPrice = price
        return order