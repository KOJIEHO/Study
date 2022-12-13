import requests
import json
from bs4 import BeautifulSoup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


# ФИО, Специализация, стаж, где прием, номер, карточки образования и курсы
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36",
    "accept": "*/*"}
url = 'https://doctu.ru/api/site/get-cities'
response = requests.get(url, timeout=30, headers=headers)
data = response.json()
city_arr = []
count = 0
while count < 110:
    city_arr += [data[count]['code']]
    count += 1

count = 0
while count < 1: # 110
    count_page = 1
    while count_page < 2: #51
        url = 'https://doctu.ru/' + str(city_arr[count]) + '/doctors?page=' + str(count_page)
        print(city_arr[count])
        response = requests.get(url, timeout=30, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')
        link_user = [
            a.get('href')
            for a in soup.find_all('a')
            if a.get('href') and a.get('href').startswith('/' + str(city_arr[count]) + '/doctor/')
        ]
        number_telephone = soup.find("div", {"class": "contact_information"}).text.split('Прием')
        print(link_user)
        print(len(link_user))
        print(number_telephone[0])

        count_user = 0
        while count_user < 1: # len(link_user)
            url = 'https://doctu.ru' + str(link_user[count_user])
            response = requests.get(url, timeout=30, headers=headers)
            soup = BeautifulSoup(response.content, 'lxml')
            Doctor_name = soup.find("h1").text.strip()
            Spec = soup.find("div", {"class": "specialty"}).text.strip()
            Experience = soup.find("div", {"class": "experience"}).text.strip()
            Clinic_name = soup.find("p", {"class": "doc-intro"}).text.split('.')
            Education = soup.find("div", {"class": "col-xs-4 education"}).text.strip()

            print(Doctor_name)
            print(Spec)
            print(Experience)
            print(Clinic_name[1].strip())
            print(Education)
            count_user += 1
        count_page += 1

    count += 1
