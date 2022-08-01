import telebot
from telebot import types  # для указание типов

bot = telebot.TeleBot('Token')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Канал")
    btn2 = types.KeyboardButton("❓ Информация")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,text='Текст новости', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Канал"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("Дашборд")
        btn5 = types.KeyboardButton("Экспорт")
        back6 = types.KeyboardButton("Внутренний рынок")
        back7 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4, btn5, back6,back7)
        bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)
    elif (message.text == "❓ Информация"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("График")
        btn2 = types.KeyboardButton("Таблица")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите действие:", reply_markup=markup)

    elif (message.text == "График"):
        bot.send_message(message.chat.id, "Вывод графиков по индексам")
        # вставить чать кода из готового бота, которая отвечает за построение и отправку графиков в тг чат

    elif message.text == "Таблица":
        bot.send_message(message.chat.id, text="Отправка файла Exel с данными")
        # Вставить чать кода из готового бота, которая отвечает за выгрузку данных из базы в эксель за заданный период
        # Добавить кнопки по необходимости для выбора диапозона или ввода диапозона


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Канал")
        button2 = types.KeyboardButton("❓ Информация")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
        # Позволит боту информировать пользователя, что писать данные просто так не стоит
        # Изменить данное условие при подключенни  функций для Дашборда

bot.polling(none_stop=True)