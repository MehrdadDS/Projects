import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_historical_data(crypto_id, start_date, end_date):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart/range'
    params = {
        'vs_currency': 'usd',
        'from': int(start_date.timestamp()),
        'to': int(end_date.timestamp())
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Extract and format the data
    prices = data['prices']
    formatted_data = [(datetime.utcfromtimestamp(price[0] / 1000).date(), price[1]) for price in prices]
    df = pd.DataFrame(formatted_data, columns=['Date', 'Price'])
    return df

def main():
    # Define the cryptocurrency IDs (as used by CoinGecko)
    crypto_ids = ['bitcoin', 'dogecoin']
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2021, 12, 31)

    for crypto_id in crypto_ids:
        print(f"Fetching data for {crypto_id}...")
        df = fetch_historical_data(crypto_id, start_date, end_date)
        df.to_csv(f'{crypto_id}_historical_prices.csv', index=False)
        print(f"Data for {crypto_id} saved to {crypto_id}_historical_prices.csv")

if __name__ == "__main__":
    main()
