import os
import errno
from time import sleep
import telebot
from telebot import types
import sqlite3
from datetime import datetime

bot = telebot.TeleBot('5505393093:AAEs2u7969d0RuQuzmwjqR0IkyHBYy0-su0')

@bot.message_handler(content_types=['text'])
def func(message):
    message_arr = message.text.split()
    markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📸 Выгрузка отчета отчет")
    # btn2 = types.KeyboardButton("📜 Примеры работ")
    # btn3 = types.KeyboardButton("🗣️ Финансовый отдел")
    btn4 = types.KeyboardButton("🧾 Выгрузка графика работы")
    # btn5 = types.KeyboardButton("📑 Правила работы")
    markup_main.add(btn1, btn4)

    markup_return = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Вернуться в главное меню")
    markup_return.add(button1)

    if message.text == "📸 Выгрузка отчета отчет":
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, text='Введите:\nОтчет\nИванов Иван Иванович', reply_markup=markup_return)



    elif message.text == "🧾 Выгрузка графика работы":
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, text=f"Введите:\nГрафик работ\nИванов Иван Иванович\n01.03.2001\n01.04.2002", reply_markup=markup_return)

    elif message_arr[0] == 'График':
        table_name = message_arr[2] + message_arr[3] + message_arr[4]
        date_range_min = message_arr[5]
        date_range_max = message_arr[6]
        print(table_name,date_range_min,date_range_max)





    elif message.text == "Вернуться в главное меню":
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup_main)
    # else:
    #     bot.delete_message(message.chat.id, message.message_id - 1)
    #     bot.delete_message(message.chat.id, message.message_id)
    #     bot.send_message(message.chat.id, text="Я вас не понимаю. Попробуйте другую команду.",
    #                      reply_markup=markup_return)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)

