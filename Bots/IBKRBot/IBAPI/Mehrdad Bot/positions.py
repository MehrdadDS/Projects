from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import *
from ibapi.contract import *
import time
import pandas as pd

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.positions = []

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

def main():
    app = IBApi()
    app.connect("127.0.0.1", 7496, 0)
    
    time.sleep(1)  # Sleep interval to allow time for connection to server
    
    app.reqPositions()  # Request positions
    
    time.sleep(5)  # Keep the script running to receive the positions
    app.run()

    # Convert positions to DataFrame
    positions_df = pd.DataFrame(app.positions)
    print(positions_df)
    
    # Save DataFrame to a CSV file
    positions_df.to_csv("positions.csv", index=False)

if __name__ == "__main__":
    main()
