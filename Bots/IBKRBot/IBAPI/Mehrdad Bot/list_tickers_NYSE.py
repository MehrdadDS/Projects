import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import time

# Monkey patching yfinance
yf.pdr_override()

def get_nyse_tickers():
    try:
        # Use Wikipedia's list of NYSE companies
        url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        tables = pd.read_html(url)
        tickers = tables[0]['Symbol'].tolist()
        return tickers
    except Exception as e:
        print(f"Could not retrieve tickers list: {e}")
        return []

nyse_tickers = get_nyse_tickers()

small_cap_tickers_less_than_50 = []
medium_cap_tickers_between_50_to_100 = []
large_cap_tickers_greater_than_100 = []

# Fetch market cap for each ticker and categorize
for ticker in nyse_tickers:
    try:
        stock = yf.Ticker(ticker)
        market_cap = stock.info.get('marketCap', None)
        if market_cap is not None:
            market_cap = market_cap / 1e9  # Convert to billions
            if market_cap < 50:
                small_cap_tickers_less_than_50.append(ticker)
            elif 50 <= market_cap <= 100:
                medium_cap_tickers_between_50_to_100.append(ticker)
            else:
                large_cap_tickers_greater_than_100.append(ticker)
    except Exception as e:
        print(f"Could not retrieve data for {ticker}: {e}")
    time.sleep(0.5)  # To avoid hitting the API rate limit

print(f"small_cap_tickers_less_than_50= {small_cap_tickers_less_than_50}")
print(f"medium_cap_tickers_between_50_to_100= {medium_cap_tickers_between_50_to_100}")
print(f"large_cap_tickers_greater_than_100= {large_cap_tickers_greater_than_100}")
