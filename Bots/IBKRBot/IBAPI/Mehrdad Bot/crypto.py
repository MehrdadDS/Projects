from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time
import pandas as pd

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = {}
        
    def historicalData(self, reqId, bar):
        if reqId not in self.data:
            self.data[reqId] = []
        self.data[reqId].append([bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume])

    def historicalDataEnd(self, reqId, start, end):
        print(f"Finished receiving historical data for request {reqId}")
        if reqId == max(app.data.keys()):  # Ensure disconnect is called after the last request is completed
            self.disconnect()

def websocket_con():
    app.run()

app = IBApi()
app.connect("127.0.0.1", 7497, clientId=1)

con_thread = threading.Thread(target=websocket_con, daemon=True)
con_thread.start()
time.sleep(1)

cryptos = [
    "BTC", "ETH", "XLM", "DOT", "SOL", "XRP", "XTZ", "ADA",
    "LTC", "TRX", "AVAX", "MATIC", "LUNA", "ALGO", "BNB", "BCH"
]

req_id = 1
for crypto in cryptos:
    contract = Contract()
    contract.symbol = crypto
    contract.secType = "CRYPTO"
    contract.exchange = "PAXOS"
    contract.currency = "USD"
    
    end_time = ""
    duration = "1 D"
    bar_size = "5 mins"
    what_to_show = "MIDPOINT"
    use_rth = 1
    format_date = 1
    
    app.reqHistoricalData(reqId=req_id, contract=contract, endDateTime=end_time, durationStr=duration,
                          barSizeSetting=bar_size, whatToShow=what_to_show, useRTH=use_rth, formatDate=format_date,
                          keepUpToDate=False, chartOptions=[])
    req_id += 1
    time.sleep(2)

# Allow some time to receive data
time.sleep(10)

# Displaying the collected data
for req_id, data in app.data.items():
    df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    print(f"Data for request {req_id}:\n", df)

app.disconnect()
