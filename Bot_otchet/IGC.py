from bs4 import BeautifulSoup
import telebot
import requests
import sqlite3
from user_id import user_id, token


bot = telebot.TeleBot(token)
URL_IGC = 'https://www.igc.int/ru/gmr_summary.aspx'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36",
    "accept": "*/*"}


def get_info_IGC():
    k = 'Просто переменная'
    response = requests.get(URL_IGC, timeout=30, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    text = soup.find("div", {"id": "TextDiv"}).text
    text = " ".join(text.split())[0:200]

    base = sqlite3.connect('IGC.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS IGC(text, header)')
    base.commit()
    cur.execute('INSERT INTO IGC VALUES(?, ?)', ('0', '0'))
    base.commit()
    r = cur.execute('SELECT text FROM IGC').fetchall()
    if r[0][0] == text:
        print('Новой статьи с IGC нет!')
    else:
        cur.execute('DELETE FROM IGC')
        base.commit()
        cur.execute('INSERT INTO IGC VALUES(?, ?)', (text, k))
        base.commit()
        print('На International Grains Council вышла новая статья!')
        news = f"_Напоминаю, что на International Grains Council вышла новая статья!_\n[{'igc.int'}]({'https://www.igc.int/ru/gmr_summary.aspx'})"
        id = 0
        while id < len(user_id):
            bot.send_message(user_id[id], news, parse_mode='Markdown', disable_web_page_preview=True)
            id += 1