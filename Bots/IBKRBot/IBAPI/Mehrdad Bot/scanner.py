from ibapi.client import *
from ibapi.wrapper import *

port = 7496

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        self.reqScannerParameters()

    def scannerParameters(self, xml):
        dir = "C:\My Folder\Github\Projects\\Bots\\IBKRBot\\IBAPI\\Mehrdad Bot\\scanner.xml"
        open(dir, 'w').write(xml)
        print("Scanner parameters received!")

app = TestApp()
app.connect("127.0.0.1", port, 1001)
app.run()
