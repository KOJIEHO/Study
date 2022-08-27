import requests
import sqlite3
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36",
    "accept": "*/*"}


# Это первый вариант
# base = sqlite3.connect('Data1.db')
# cur = base.cursor()
# base.execute('CREATE TABLE IF NOT EXISTS TABLE1(Id, Array_photo_links, Model, Badge, FuelType, FormYear, Mileage, OfficeCityState, Price, Manufacturer)')
# base.commit()
# count = 0  # Это фактически номер страницы, но надо делать +1, тогда будет номер. Всего 157 полных и 156 неполная страница
# while count < 158: # 158
#     url = 'http://api.encar.com/search/car/list/premium?count=true&q=(And.Year.range(201800..202299)._.Mileage.range(10000..70000)._.Hidden.N._.CarType.Y._.Trust.Warranty._.Condition.Inspection._.(Or.FuelType.%EB%94%94%EC%A0%A4._.FuelType.%EA%B0%80%EC%86%94%EB%A6%B0.)_.Transmission.%EC%98%A4%ED%86%A0.)&sr=%7CModifiedDate%7C' + str(count * 50) + '%7C50'
#     count += 1
#     response = requests.get(url, timeout=30, headers=headers)
#     data = response.json()
#     count_for_each_page = 0
#     while count_for_each_page < len(data['SearchResults']):
#         Id = str(data['SearchResults'][count_for_each_page]['Id'])
#         count_for_photo = 0
#         Array_photo_links = []
#         while count_for_photo < len(data['SearchResults'][count_for_each_page]['Photos']):
#             Array_photo_links += ['http://ci.encar.com/carpicture' + str(data['SearchResults'][count_for_each_page]['Photos'][count_for_photo]['location']) + '?impolicy=heightRate&rh=91&cw=122&ch=91&cg=Center&wtmk=http://ci.encar.com/wt_mark/w_mark_03.png&wtmkg=SouthEast&wtmkw=45&wtmkh=12.3']
#             count_for_photo += 1
#         Array_photo_links = str(Array_photo_links)
#         Manufacturer = str(data['SearchResults'][count_for_each_page]['Manufacturer'])
#         Model = str(data['SearchResults'][count_for_each_page]['Model'])
#         Badge = str(data['SearchResults'][count_for_each_page]['Badge'])
#         FuelType = str(data['SearchResults'][count_for_each_page]['FuelType'])
#         FormYear = str(data['SearchResults'][count_for_each_page]['FormYear'])
#         Mileage = str(data['SearchResults'][count_for_each_page]['Mileage'])
#         OfficeCityState = str(data['SearchResults'][count_for_each_page]['OfficeCityState'])
#         Price = str(data['SearchResults'][count_for_each_page]['Price'])
#         cur.execute('INSERT INTO TABLE1 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (Id, Array_photo_links, Model, Badge, FuelType, FormYear, Mileage, OfficeCityState, Price, Manufacturer))
#         base.commit()
#         count_for_each_page += 1
#         print('##########################################')
#         print('Страница: ' + str(count) + '  Машина номер: ' + str(count_for_each_page))
#         print('Id = ' + Id + '\nArray_photo_links = ' + Array_photo_links + '\nManufacturer = ' + Manufacturer + '\nModel = ' + Model + '\nBadge = ' + Badge + '\nFuelType = ' + FuelType + '\nFormYear = ' + str(FormYear) + '\nMileage = ' + str(Mileage) + '\nOfficeCityState = ' + OfficeCityState + '\nPrice = ' + str(Price))
#         print('##########################################')


# Это второй вариант
base = sqlite3.connect('Data2.db')
cur = base.cursor()
base.execute('CREATE TABLE IF NOT EXISTS TABLE1(Id, Array_photo_links, Model, Badge, FuelType, FormYear, Mileage, OfficeCityState, Price, Manufacturer)')
base.commit()
count = 0  # Это фактически номер страницы, но надо делать +1, тогда будет номер. Всего 75 полных и 76 неполная страница
while count < 76: # 76
    try:
        url = 'http://api.encar.com/search/car/list/premium?count=true&q=(And.Year.range(201800..202299)._.Mileage.range(10000..70000)._.Hidden.N._.CarType.N._.Trust.Warranty._.Condition.Inspection._.(Or.FuelType.%EB%94%94%EC%A0%A4._.FuelType.%EA%B0%80%EC%86%94%EB%A6%B0.)_.Transmission.%EC%98%A4%ED%86%A0.)&sr=%7CModifiedDate%7C' + str(count * 50) + '%7C50'
        count += 1
        response = requests.get(url, timeout=30, headers=headers)
        data = response.json()
        count_for_each_page = 0
        while count_for_each_page < len(data['SearchResults']):
            Id = str(data['SearchResults'][count_for_each_page]['Id'])
            count_for_photo = 0
            Array_photo_links = []
            while count_for_photo < len(data['SearchResults'][count_for_each_page]['Photos']):
                Array_photo_links += ['http://ci.encar.com/carpicture' + str(data['SearchResults'][count_for_each_page]['Photos'][count_for_photo]['location']) + '?impolicy=heightRate&rh=91&cw=122&ch=91&cg=Center&wtmk=http://ci.encar.com/wt_mark/w_mark_03.png&wtmkg=SouthEast&wtmkw=45&wtmkh=12.3']
                count_for_photo += 1
            Array_photo_links = str(Array_photo_links)
            Manufacturer = str(data['SearchResults'][count_for_each_page]['Manufacturer'])
            Model = str(data['SearchResults'][count_for_each_page]['Model'])
            Badge = str(data['SearchResults'][count_for_each_page]['Badge'])
            FuelType = str(data['SearchResults'][count_for_each_page]['FuelType'])
            FormYear = str(data['SearchResults'][count_for_each_page]['FormYear'])
            Mileage = str(data['SearchResults'][count_for_each_page]['Mileage'])
            OfficeCityState = str(data['SearchResults'][count_for_each_page]['OfficeCityState'])
            Price = str(data['SearchResults'][count_for_each_page]['Price'])
            cur.execute('INSERT INTO TABLE1 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (Id, Array_photo_links, Model, Badge, FuelType, FormYear, Mileage, OfficeCityState, Price, Manufacturer))
            base.commit()
            count_for_each_page += 1
            print('##########################################')
            print('Страница: ' + str(count) + '  Машина номер: ' + str(count_for_each_page))
            print('Id = ' + Id + '\nArray_photo_links = ' + Array_photo_links + '\nManufacturer = ' + Manufacturer + '\nModel = ' + Model + '\nBadge = ' + Badge + '\nFuelType = ' + FuelType + '\nFormYear = ' + str(FormYear) + '\nMileage = ' + str(Mileage) + '\nOfficeCityState = ' + OfficeCityState + '\nPrice = ' + str(Price))
            print('##########################################')
    except Exception:
        continue
