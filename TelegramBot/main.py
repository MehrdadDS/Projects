import requests
from telegram import Bot
import schedule
import time

# Telegram bot API token
TOKEN = ""

# Your cryptocurrency portfolio
portfolio = {
    'BTC': 1,
    'ETH': 2,
    'ADA': 10
}

# Function to fetch cryptocurrency prices
def get_prices():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano&vs_currencies=usd")
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to calculate portfolio value
def calculate_portfolio_value(prices):
    total_value = 0
    for coin, amount in portfolio.items():
        total_value += amount * prices[coin]['usd']
    return total_value

# Function to send message
def send_portfolio_value():
    prices = get_prices()
    if prices:
        total_value = calculate_portfolio_value(prices)
        bot = Bot(TOKEN)
        bot.send_message(chat_id='Mehrdadportfo_bot', text=f"Your portfolio value: ${total_value:.2f}")

# Schedule message sending every minute
schedule.every().minute.do(send_portfolio_value)

while True:
    schedule.run_pending()
    time.sleep(1)
