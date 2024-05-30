import telebot
bot = telebot.TeleBot('6973724292:AAH4XTP3y1a-6EKi0yFBcqfSR45TsznSMJI')

class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot('6973724292:AAH4XTP3y1a-6EKi0yFBcqfSR45TsznSMJI')
    

    def tlg_send_message(message):
        bot.send_message(83167574, text=message, parse_mode='Markdown')

