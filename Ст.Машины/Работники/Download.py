import os
import errno
from time import sleep
import telebot
from telebot import types
import sqlite3
from datetime import datetime

bot = telebot.TeleBot('5505393093:AAEs2u7969d0RuQuzmwjqR0IkyHBYy0-su0')#Токен от бота "КСМ"

@bot.message_handler(content_types=['text'])
def func(message):
    message_arr = message.text.split()
    markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📸 Выгрузка отчета отчет")
    btn4 = types.KeyboardButton("🧾 Выгрузка графика работы")
    markup_main.add(btn1, btn4)

    markup_return = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Вернуться в главное меню")
    markup_return.add(button1)


    #Пример ввода текста для выгрузки отчета
    if message.text == "📸 Выгрузка отчета отчет":
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, text='Введите:\nОтчет\nИванов Иван Иванович', reply_markup=markup_return)


    # Пример ввода текста для выгрузки графика работы
    elif message.text == "🧾 Выгрузка графика работы":
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, text=f"Введите:\nГрафик работ\nИванов Иван Иванович\n01.03.2001\n01.04.2002", reply_markup=markup_return)

    #Отлов сообщения для выгрузки графика работы
    elif message_arr[0] == 'График':

        message_arr[2].replace(' ', '')
        message_arr[3].replace(' ', '') # пытался удалить все ебаные пробелы
        message_arr[4].replace(' ', '')

        # переменная, принимающая значение ФИО без пробелов
        # Из Курнаев Данила Владимирович делает и запоминает ввиде -> КурнаевДанилаВладимирович
        # Текст сообщения, который ввожу:
        # График работ
        # Курнаев Данила Владимирович
        # 01.03.2001
        # 01.04.2002
        # Даты планировал использовать для выбора диапозона вывода, но думаю нахуй это ненужно, пусть выводиться все, что накопилось в бд
        table_name_person = message_arr[2] + message_arr[3] + message_arr[4]

        date_range_min = message_arr[5]
        date_range_max = message_arr[6]# Диапозоны, которые хотел использовать, даты записываются

        table_name_person[0][0].replace(' ', '')
        print(len(table_name_person))
        e = 'КурнаевДанилаВладимирович' # название таблицы, скопировал из бд
        print(len(e))
        print(table_name_person, date_range_min, date_range_max)

        base = sqlite3.connect('GrafikRaboti.db')
        cur = base.cursor()                                 # Я не понимаю хули не подключается, все должно сходиться
        info_Grafik_list = cur.execute('SELECT * FROM ' + table_name_person).fetchall()
        print(info_Grafik_list)
        #Планирую просто выгрузить в список все данные из бд
        # и засунуть построчно в бд,
        # пробегась циклом по всей длинне,
        # этот файл отправлять и все


    elif message.text == "Вернуться в главное меню":
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup_main)
    # else:
    #     bot.delete_message(message.chat.id, message.message_id - 1)
    #     bot.delete_message(message.chat.id, message.message_id)
    #     bot.send_message(message.chat.id, text="Я вас не понимаю. Попробуйте другую команду.",
    #                      reply_markup=markup_return)


    #Трай решает проблему с отрублением после 5 минут простоя!
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)

