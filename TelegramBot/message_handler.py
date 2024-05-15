import telebot


bot = telebot.TeleBot('..')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,'welcome to Mehrdad bot.')
    bot.reply_to(message,'This is a reply')
    bot.register_next_step_handler(message,process_name)

def process_name(message):
    name = message.text
    bot.send_message(message.chat.id,f"Hello {name}! this is going to be a test")

    bot.register_next_step_handler(message,process_age)

def process_age(message):
    age = message.text
    bot.send_message(message.chat.id,f"you are {age} years old.")
bot.polling()

