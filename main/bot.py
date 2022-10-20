import telebot
import schedule
from config import token


class T_Bot:
    chat_id = ''

    def __init__(self):
        self.bot = telebot.TeleBot(token)

    def _send_files_(self):
        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            self.chat_id = message.chat.id
            self.start = schedule.every(300).seconds.do()

    def _stop_(self):
        @self.bot.message_handler(commands=['stop'])
        def stop_message(message):
            schedule.clear()

    def send_file(self, file):
        send_file = open(file)
        self.bot.send_photo(self.chat_id, send_file)
