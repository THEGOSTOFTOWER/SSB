import telebot

from sqlite.py import Sql
bot = telebot.TeleBot('1674405414:AAHDYbRGyi41qRWlLuDe1zkYCcvLmwKaMHQ')
db = Sql('db.db')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')
bot.polling()
