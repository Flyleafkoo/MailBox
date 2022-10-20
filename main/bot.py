import telebot
import give_attachment
from config import token
import schedule

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    filenames = give_attachment.get_attachment
    for file in filenames:
        send_file = open(file)
        bot.send_photo(message.chat.id, send_file)


bot.polling()
