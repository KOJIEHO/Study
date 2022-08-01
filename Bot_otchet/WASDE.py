from bs4 import BeautifulSoup
import telebot
import requests
from user_id import user_id, token


bot = telebot.TeleBot(token)
URL_WASDE1 = 'https://www.usda.gov/oce/commodity/wasde'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36",
    "accept": "*/*"}


def get_info_WASDE():
    try:
        response = requests.get(URL_WASDE1, timeout=30, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')

        link_for_pdf = [
                a.get('href')
                for a in soup.find_all('a')
                if a.get('href') and a.get('href').startswith('https://www.usda.gov/oce/commodity/wasde/')
            ][0:1]
        # link_for_pdf = 'https://www.usda.gov/oce/commodity/wasde/wasde0622.pdf' # Тут записан пдф файл прошлой статьи

        r = requests.get(link_for_pdf, timeout=30, headers=headers)
        with open('WASDE.pdf', "wb") as code:
            code.write(r.content)
        print('На The World Agricultural Supply and Demand Estimates (WASDE) вышла новая статья!')
        news = f"_Напоминаю, что на The World Agricultural Supply and Demand Estimates (WASDE) вышла новая статья!_\n[{'WASDE'}]({'https://www.usda.gov/oce/commodity/wasde'})"
        id = 0
        while id < len(user_id):
            bot.send_message(user_id[id], news, parse_mode='Markdown', disable_web_page_preview=True)
            bot.send_document(chat_id=user_id[id], document=open('WASDE.pdf', 'rb'))
            id += 1
    except:
        print('Новой статьи с WASDE нет!')