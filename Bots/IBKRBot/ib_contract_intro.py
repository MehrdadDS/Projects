# -*- coding: utf-8 -*-
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        
    def error(self, reqId, errorCode, errorString):
        print("Error {} {} {}".format(reqId,errorCode,errorString))
        
    def contractDetails(self, reqId, contractDetails):
        print("redID: {}, contract:{}".format(reqId,contractDetails))

    
app = TradingApp()      
app.connect("127.0.0.1", 7496, clientId=1)

contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"

app.reqContractDetails(100, contract)
app.run()


    