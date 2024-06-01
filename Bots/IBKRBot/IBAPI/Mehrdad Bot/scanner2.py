from ibapi.client import *
from ibapi.wrapper import *
from ibapi.tag_value import *

port = 7496

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.tickers = []

    def nextValidId(self, orderId: int):
        sub = ScannerSubscription()
        sub.instrument = "STK"
        sub.locationCode = "STK.US.MAJOR"
        
        sub.locationCode = "STK.NASDAQ"
        #sub.scanCode = "TOP_TRADE_COUNT"
        sub.scanCode = "TOP_OPEN_PERC_GAIN"

        scan_options = []
        filter_options = [
            TagValue("volumeAbove", "100000"),
            TagValue("marketCapAbove1e6", "100"),
            #TagValue("priceAbove", "1")
        ]

        self.reqScannerSubscription(orderId, sub, scan_options, filter_options)

    def scannerData(self, reqId, rank, contractDetails, distance, benchmark, projection, legsStr):
        ticker = contractDetails.contract.symbol
        self.tickers.append(ticker)
        print(f"scannerData. reqId: {reqId}, ticker: {ticker}, distance: {distance}, benchmark: {benchmark}, projection: {projection}, legsStr: {legsStr}")

    def scannerDataEnd(self, reqId):
        self.cancelScannerSubscription(reqId)
        self.disconnect()
        print(f"scannerDataEnd. reqId: {reqId}")
        print("Tickers:", self.tickers)

def main():
    app = TestApp()
    app.connect("127.0.0.1", port, 0)
    app.run()

if __name__ == "__main__":
    main()
