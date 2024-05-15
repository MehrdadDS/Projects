import telebot


bot = telebot.TeleBot('..')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,'welcome to Mehrdad bot.')
    bot.reply_to(message,'This is a reply')
bot.polling()