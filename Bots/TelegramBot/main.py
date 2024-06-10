import requests
import functools
import time
import telebot

bot = telebot.TeleBot('6973724292:AAH4XTP3y1a-6EKi0yFBcqfSR45TsznSMJI')

# Telegram bot API token
TOKEN = "6973724292:AAH4XTP3y1a-6EKi0yFBcqfSR45TsznSMJI"

# Your cryptocurrency portfolio
portfolio = {
    'bitcoin': 1,
    'ethereum': 2,
    'cardano': 1058,
    'dogecoin':3115,
    #'polygon':1020,
    #'xrp':2288
}

# Function to fetch cryptocurrency prices
def get_prices():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano,dogecoin&vs_currencies=usd")
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to calculate portfolio value
def calculate_portfolio_value(prices):
    total_value = 0
    coin_values = {}
    for coin, amount in portfolio.items():
        coin_values[coin] = amount * prices[coin]['usd']
        total_value += coin_values[coin]
    return total_value, coin_values

# Function to send message
def send_portfolio_value(bot):
    prices =""
    prices = get_prices()
    if prices:
        total_value, coin_values = calculate_portfolio_value(prices)
        coin_values_message = "\n".join([f"- **{coin}**: ${int(value)}" for coin, value in coin_values.items()])
        message = f"Your portfolio value: ${int(total_value)}\n---\n{coin_values_message}"
        bot.send_message(83167574, text=message, parse_mode='Markdown')

# Infinite loop to fetch prices and send messages every second
while True:
    send_portfolio_value(bot)
    time.sleep(310)
