from bs4 import BeautifulSoup
import telebot
import requests
from user_id import user_id, token
import datetime


bot = telebot.TeleBot(token)
URL_AMIS1 = 'http://www.amis-outlook.org/amis-monitoring/monthly-report/en/#.YsZ_QHZBxPZ'
date_str = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36",
    "accept": "*/*"}


def get_info_AMIS():
    response1 = requests.get(URL_AMIS1, timeout=30, headers=headers)
    soup = BeautifulSoup(response1.content, 'lxml')

    link_for_pdf = [
        a.get('href')
        for a in soup.find_all('a')
        if a.get('href') and a.get('href').startswith('')
    ][31:32]
    response2 = requests.get(link_for_pdf[0], timeout=30, headers=headers)
    with open('AMIS.pdf', "wb") as code:
        code.write(response2.content)

    datenow = str(datetime.datetime.now())[5:][:5]
    date_AMIS = str(soup.find("div", {"id": "c208738"}))[335:][:99]
    date_AMIS = date_AMIS.split(",")

    count = 0
    while count < len(date_AMIS):
        date_AMIS[count] = date_AMIS[count].split()
        count += 1

    count = 0
    while count < len(date_AMIS):
        if len(date_AMIS[count][1]) == 1:
            date_AMIS[count][1] = str('0' + date_AMIS[count][1])
        count += 1

    count = 0
    while count < len(date_AMIS):
        if date_AMIS[count][0] == date_str[0]:
            date_AMIS[count][0] = '01'
        elif date_AMIS[count][0] == date_str[1]:
            date_AMIS[count][0] = '02'
        elif date_AMIS[count][0] == date_str[2]:
            date_AMIS[count][0] = '03'
        elif date_AMIS[count][0] == date_str[3]:
            date_AMIS[count][0] = '04'
        elif date_AMIS[count][0] == date_str[4]:
            date_AMIS[count][0] = '05'
        elif date_AMIS[count][0] == date_str[5]:
            date_AMIS[count][0] = '06'
        elif date_AMIS[count][0] == date_str[6]:
            date_AMIS[count][0] = '07'
        elif date_AMIS[count][0] == date_str[7]:
            date_AMIS[count][0] = '08'
        elif date_AMIS[count][0] == date_str[8]:
            date_AMIS[count][0] = '09'
        elif date_AMIS[count][0] == date_str[9]:
            date_AMIS[count][0] = '10'
        elif date_AMIS[count][0] == date_str[10]:
            date_AMIS[count][0] = '11'
        elif date_AMIS[count][0] == date_str[11]:
            date_AMIS[count][0] = '12'
        count += 1

    count = 0
    while count < len(date_AMIS):
        date_AMIS[count] = str(date_AMIS[count][0] + '-' + date_AMIS[count][1])
        count += 1

    # datenow = '07-08'
    count = 0
    k = 0
    while count < len(date_AMIS):
        if date_AMIS[count] == datenow:
            k = 1
            print('На на AMIS Market Monitor вышла новая статья!')
            news = f"_Напоминаю, что сегодня выходит статья на AMIS Market Monitor!_\n[{'AMIS Market Monitor'}]({'http://www.amis-outlook.org/amis-monitoring/monthly-report/en/#.YsZ_QHZBxPZ'})"
            id = 0
            while id < len(user_id):
                bot.send_message(user_id[id], news, parse_mode='Markdown', disable_web_page_preview=True)
                bot.send_document(chat_id=user_id[id], document=open('AMIS.pdf', 'rb'))
                id += 1
        count += 1
    if k != 1:
        print('Новой статьи с AMIS нет!')