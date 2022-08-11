import os
import errno
from datetime import datetime
import json
import telebot
from telebot import types  # для указание типов
bot = telebot.TeleBot('5505393093:AAEs2u7969d0RuQuzmwjqR0IkyHBYy0-su0')

otchet_time = str(datetime.now().hour) + '-' + str(datetime.now().minute) + ' ; ' + str(datetime.now().date())

def make_sure_path_exists(path):
    try: os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

@bot.message_handler(content_types=["photo"])
def handle_docs_photo(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Вернуться в главное меню")
    markup.add(button1)
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)



        src = f'C:\\Users\danil\\PycharmProjects\\pythonProject\\{str(chat_id)}\\{otchet_time}.png'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Фото добавлено", reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, e)

@bot.message_handler(commands=['start'])
def start(message):
    markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📸 Отчет")
    btn2 = types.KeyboardButton("📜 Примеры работ")
    btn3 = types.KeyboardButton("🗣️ Финансовый отдел")
    btn4 = types.KeyboardButton("🧾 График работы")
    btn5 = types.KeyboardButton("📑 Правила работы")
    markup_main.add(btn1, btn2, btn3, btn4, btn5)

    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, text='👋Добрый день, Я - Бот компании Ст.машины', reply_markup=markup_main)

@bot.message_handler(content_types=['text'])
def func(message):

    markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📸 Отчет")
    btn2 = types.KeyboardButton("📜 Примеры работ")
    btn3 = types.KeyboardButton("🗣️ Финансовый отдел")
    btn4 = types.KeyboardButton("🧾 График работы")
    btn5 = types.KeyboardButton("📑 Правила работы")
    markup_main.add(btn1, btn2, btn3, btn4, btn5)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Вернуться в главное меню")
    markup.add(button1)
    soobshenie = str(message.text)
    if (message.text == "📸 Отчет"):
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.send_message(message.chat.id, text='Пришлите в чат фотографию акта или бланка, а также описание:', reply_markup=markup)
        make_sure_path_exists(str(message.chat.id))
        bot.send_message(message.chat.id,
                         text='Введите Описание по примеру:\nОписание\n(ВМ)Балашиха новая Павлина ул.Троицкая д2 кв186 под3 эт13.  Александр. Сантехник.  Установить ванну. Си нужен сегодня',
                         reply_markup=markup)
    elif soobshenie.find('Описание') != -1:
        print('описание получил',soobshenie)
        data = f'{str(message.chat.id)} : {otchet_time} : {soobshenie}\n'# вот это надо в бд, название таблицы по перой переменной, вторы две переменные столбцы базы
        with open('Otchet.txt', 'a', encoding = 'utf8') as file:
            json.dump(data, file, indent=0, ensure_ascii=False)
        print('Пришлите в чат фотографию акта или бланка')
        bot.delete_message(message.chat.id, message.message_id)
    elif (message.text == "📜 Примеры работ"):
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.send_message(message.chat.id, text=f"Есть несколько готовых актов:\n_ТУТ ДОЛЖнЫ БЫТЬ ФОТОГРАФИИ_", reply_markup=markup)
        print(f"Есть несколько готовых актов:\n_ТУТ ДОЛЖнЫ БЫТЬ ФОТОГРАФИИ_")
        bot.delete_message(message.chat.id, message.message_id)

    elif (message.text == "🧾 График работы"):
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.send_message(message.chat.id, "Пришлите график своей работы:\nСообщение по примеру\n*Пример*", reply_markup=markup)
        print("Пришлите график своей работы:\nСообщение по примеру\n*Пример*")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text == "🗣️ Финансовый отдел":
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.send_message(message.chat.id, text="Для связи с куратором с куратором обратитесь сюда: \n@finotdelSC",reply_markup=markup)
        print("Для связи с куратором с куратором обратитесь сюда: \n@KurnaevDV\n@Отдел логистики Ст.машины Fl.ru")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text == "📑 Правила работы":
        bot.delete_message(message.chat.id, message.message_id-1)
        with open('Rules.txt', 'r',encoding='utf8') as new_file:
            rule = new_file.read()
        bot.send_message(message.chat.id, text=f"Перечень правил работы:\n{rule}",reply_markup=markup)
        print(f"Перечень правил работы:\n{rule}")
        bot.delete_message(message.chat.id, message.message_id)

    elif (message.text == "Вернуться в главное меню"):
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup_main)
        print("Вы вернулись в главное меню")
        # bot.delete_message(message.chat.id, message.message_id)

    # else:
    #     bot.delete_message(message.chat.id, message.message_id)
    #     bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..", reply_markup=markup)
    #     print("На такую комманду я не запрограммировал..")
    #     bot.delete_message(message.chat.id, message.message_id-1)

bot.polling(none_stop=True)



# мой айди - 693852768