import backtrader as bt
from datetime import datetime
from ib_insync import IB, util, Stock

# Define the strategy
class SmaCross(bt.Strategy):
    params = (('short_period', 10), ('long_period', 30),)

    def __init__(self):
        self.short_sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.short_period)
        self.long_sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.long_period)

    def next(self):
        if self.short_sma > self.long_sma and not self.position:
            self.buy()
        elif self.short_sma < self.long_sma and self.position:
            self.sell()

# Connect to IB
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Use appropriate IP, port, and clientId

# Define IB data feed
class IBData(bt.feeds.PandasData):
    params = (('datetime', None), ('open', 'open'), ('high', 'high'),
              ('low', 'low'), ('close', 'close'), ('volume', 'volume'),
              ('openinterest', -1),)

def fetch_ib_data():
    contract = Stock('AAPL', 'SMART', 'USD')
    bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='1 D',
                                barSizeSetting='1 min', whatToShow='TRADES', useRTH=True)
    dataframe = util.df(bars)
    dataframe['datetime'] = dataframe.index
    return dataframe

data = fetch_ib_data()

# Create a Data Feed
datafeed = IBData(dataname=data)

# Initialize Cerebro engine
cerebro = bt.Cerebro()

# Add strategy to Cerebro
cerebro.addstrategy(SmaCross)

# Add data feed to Cerebro
cerebro.adddata(datafeed)

# Set broker cash
cerebro.broker.set_cash(100000)

# Set commission
cerebro.broker.setcommission(commission=0.001)

# Print starting cash
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Run backtest
cerebro.run()

# Print ending cash
print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Plot the result
cerebro.plot()
