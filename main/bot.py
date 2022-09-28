import telebot
import give_attachment
from config import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])  # keyboard
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Заявление справка 2-НДФЛ', callback_data=1))
    bot.send_message(message.chat.id, text='Выберите заявление', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Please wait!')
    if call.data == '1':
        c = give_attachment.get_attachment
        for a in c():
            photo = open(a)

            bot.send_photo(call.message.chat.id, photo)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


bot.polling()
