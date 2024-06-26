# telegrambot.py

import requests

class TelegramBot:
    def __init__(self):
        self.bot_token = "6973724292:AAH4XTP3y1a-6EKi0yFBcqfSR45TsznSMJI"
        self.chat_id = "83167574"

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
        if signal :
            formatted_message = f"""
            Ticker: {signal['ticker']}
            Time Frame: {signal['time_frame']}
            Trade Trigger: {signal['trade_trigger']}
            Entry Point: {signal['entry_point']}
            Stop Loss: {signal['stoploss']}
            Target: {signal['target']}
            Risk to Reward: {signal['risk_to_reward']}
            """
        else:
            formatted_message = f"""
            Ticker: None
            """

        return formatted_message
