import requests
import csv
import sqlite3
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36",
    "accept": "*/*"}
# /carpicture06/pic3216/32166772_
# http://ci.encar.com/carpicture +  Тут Вставка 'из Джосн  + 001.jpg?impolicy=heightRate&rh=91&cw=122&ch=91&cg=Center&wtmk=http://ci.encar.com/wt_mark/w_mark_03.png&wtmkg=SouthEast&wtmkw=45&wtmkh=12.3


# with open("Data1.csv", "a", newline="") as file:
#     writer = csv.writer(file, delimiter=";")
#     writer.writerow(
#         ["Id", "LinkPhoto", "Model", "Badge", "Transmission", "FuelType", "FormYear", "Mileage", "OfficeCityState", "Price", "Manufacturer"]
#     )
base = sqlite3.connect('Data1.db')
cur = base.cursor()
base.execute('CREATE TABLE IF NOT EXISTS TABLE1(Id, LinkPhoto, Model, Badge, Transmission, FuelType, FormYear, Mileage, OfficeCityState, Price, Manufacturer)')
base.commit()
count = 0  # Это фактически номер страницы, но надо делать +1, тогда будет номер. Всего 156 полных и 157 неполная страница
while count < 1: # 157
    url = 'http://api.encar.com/search/car/list/premium?count=true&q=(And.Year.range(201800..202299)._.Mileage.range(10000..70000)._.Hidden.N._.CarType.Y._.Trust.Warranty._.Condition.Inspection._.(Or.FuelType.%EB%94%94%EC%A0%A4._.FuelType.%EA%B0%80%EC%86%94%EB%A6%B0.)_.Transmission.%EC%98%A4%ED%86%A0.)&sr=%7CModifiedDate%7C' + str(count * 50) + '%7C50'
    count += 1
    response = requests.get(url, timeout=30, headers=headers)
    data = response.json()
    count_for_each_page = 0
    while count_for_each_page < len(data['SearchResults']):
        # Photo = requests.get('http://ci.encar.com/carpicture' +  str(LinkPhoto)  + '001.jpg?impolicy=heightRate&rh=91&cw=122&ch=91&cg=Center&wtmk=http://ci.encar.com/wt_mark/w_mark_03.png&wtmkg=SouthEast&wtmkw=45&wtmkh=12.3')
        # Photo_option = open('Страница-' + str(count) + ' Машина номер-' + str(count_for_each_page + 1) + '.jpg', 'wb')
        # Photo_option.write(Photo.content)
        # Photo_option.close()
        Id = str(data['SearchResults'][count_for_each_page]['Id'])
        LinkPhoto = str('http://ci.encar.com/carpicture' + str(data['SearchResults'][count_for_each_page]['Photo']) + '001.jpg?impolicy=heightRate&rh=91&cw=122&ch=91&cg=Center&wtmk=http://ci.encar.com/wt_mark/w_mark_03.png&wtmkg=SouthEast&wtmkw=45&wtmkh=12.3')
        Manufacturer = str(data['SearchResults'][count_for_each_page]['Manufacturer'])
        Model = str(data['SearchResults'][count_for_each_page]['Model'])
        Badge = str(data['SearchResults'][count_for_each_page]['Badge'])
        Transmission = str(data['SearchResults'][count_for_each_page]['Transmission'])
        FuelType = str(data['SearchResults'][count_for_each_page]['FuelType'])
        FormYear = str(data['SearchResults'][count_for_each_page]['FormYear'])
        Mileage = str(data['SearchResults'][count_for_each_page]['Mileage'])
        OfficeCityState = str(data['SearchResults'][count_for_each_page]['OfficeCityState'])
        Price = str(data['SearchResults'][count_for_each_page]['Price'])
        cur.execute('INSERT INTO TABLE1 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (Id, LinkPhoto, Model, Badge, Transmission, FuelType, FormYear, Mileage, OfficeCityState, Price, Manufacturer))
        base.commit()
        # with open("Data1.csv", "a", encoding='utf-16', newline="") as file:
        #     writer = csv.writer(file, delimiter=";")
        #     writer.writerow(
        #         # [Id, LinkPhoto, Model, Badge, Transmission, FuelType, FormYear, Mileage, OfficeCityState, Price, Manufacturer]
        #         [Id, LinkPhoto, '경기']
        #     )
        count_for_each_page += 1
        print('##########################################')
        print('Страница: ' + str(count) + '  Машина номер: ' + str(count_for_each_page))
        print('Id = ' + Id + '\nLinkPhoto = ' + LinkPhoto + '\nManufacturer = ' + Manufacturer + '\nModel = ' + Model + '\nBadge = ' + Badge + '\nTransmission = ' + Transmission + '\nFuelType = ' + FuelType + '\nFormYear = ' + str(FormYear) + '\nMileage = ' + str(Mileage) + '\nOfficeCityState = ' + OfficeCityState + '\nPrice = ' + str(Price))
        print('##########################################')
