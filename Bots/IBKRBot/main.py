import time
from ib_insync import *
import pandas as pd
from playsound import playsound

# Connect to IBKR TWS or IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)

# Define the stock you want to trade
stock = Stock('AAPL', 'SMART', 'USD')


# Function to calculate SMA
def calculate_sma(data, window):
    return data['close'].rolling(window=window).mean()

# Function to calculate MACD and signal line
def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
    fast_ema = data['close'].ewm(span=fast_period, min_periods=fast_period).mean()
    slow_ema = data['close'].ewm(span=slow_period, min_periods=slow_period).mean()
    macd = fast_ema - slow_ema
    signal = macd.ewm(span=signal_period, min_periods=signal_period).mean()
    return macd, signal



# Fetch historical data
def fetch_historical_data(stock, duration, bar_size):
    bars = ib.reqHistoricalData(
        stock, endDateTime='', durationStr=duration,
        barSizeSetting=bar_size, whatToShow='MIDPOINT', useRTH=True
    )
    df = util.df(bars)
    return df



# Function to check entry conditions
def check_entry_conditions(stock):
    data_4h = fetch_historical_data(stock, '30 D', '4 hours')
    data_1h = fetch_historical_data(stock, '30 D', '1 hour')
    
    data_4h['SMA34'] = calculate_sma(data_4h, 34)
    data_1h['SMA131'] = calculate_sma(data_1h, 131)
    data_4h['MACD'], data_4h['Signal'] = calculate_macd(data_4h)

    # Check if latest closing price is above SMAs
    latest_close_4h = data_4h.iloc[-1]['close']
    latest_sma34_4h = data_4h.iloc[-1]['SMA34']
    latest_close_1h = data_1h.iloc[-1]['close']
    latest_sma131_1h = data_1h.iloc[-1]['SMA131']

    # Check for MACD cross
    macd_cross = data_4h['MACD'].iloc[-2] < data_4h['Signal'].iloc[-2] and data_4h['MACD'].iloc[-1] > data_4h['Signal'].iloc[-1]

    if latest_close_4h > latest_sma34_4h and latest_close_1h > latest_sma131_1h and macd_cross:
        return True
    return False




# Function to place an order
def place_order(stock, action, quantity):
    order = MarketOrder(action, quantity)
    trade = ib.placeOrder(stock, order)
    ib.sleep(1)  # Give some time for the order to be processed
    return trade


# Function to monitor for exit conditions
def monitor_exit(trade, target_profit_percent=5):
    entry_price = trade.orderStatus.avgFillPrice
    target_price = entry_price * (1 + target_profit_percent / 100)
    while True:
        current_price = ib.reqMktData(stock, '', False, False).last
        if current_price >= target_price:
            place_order(stock, 'SELL', trade.orderStatus.filled)
            playsound('exit_trade.mp3')  # Play exit trade sound
            print(f"Exited trade at {current_price} for a profit of {target_profit_percent}%")
            break
        time.sleep(60)  # Check every minute


# Main trading loop
while True:
    if check_entry_conditions(stock):
        trade = place_order(stock, 'BUY', 100 / fetch_historical_data(stock, '1 D', '1 day').iloc[-1]['close'])
        playsound('enter_trade.mp3')  # Play enter trade sound
        monitor_exit(trade)
    time.sleep(60 * 60)  # Check conditions every hour