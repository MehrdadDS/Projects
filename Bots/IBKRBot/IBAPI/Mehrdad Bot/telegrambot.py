# telegrambot.py

import requests

class TelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def tlg_send_message(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, data=data)

    @staticmethod
    def format_signal(signal):
        formatted_message = f"""
        Ticker: {signal['ticker']}
        Time Frame: {signal['time_frame']}
        Trade Trigger: {signal['trade_trigger']}
        Entry Point: {signal['entry_point']}
        Stop Loss: {signal['stoploss']}
        Target: {signal['target']}
        Risk to Reward: {signal['risk_to_reward']}
        """
        return formatted_message
