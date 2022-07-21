from aiogram import Bot, types
from PIL import Image, ImageDraw, ImageFont
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3

# #7ed957 - Зеленый
#  - Серый
#  - Красный

token = '5320075172:AAHuXoYhg3s-TNEdDpo7F9Y_3sPThMtLnNY'
bot = Bot(token=token)
db = Dispatcher(bot)


message_arr = ['', '20.07.2022', '12 300', '14 700', '12 600', '13 600', '12 300', '14 600', '12 600', '13 600', '12 300', '14 600', '12 600', '13 600', '12 600', '13 600', '12 600', '13 600']


@db.message_handler()
async def textnew(message: types.Message):
    id = message.chat.id
    message_arr = message.text.split()

    # Внутренний рынок
    if str(message_arr[0]) == 'Рынок':
        base = sqlite3.connect('PhotoEksport.db')
        cur = base.cursor()
        image = Image.open("ЭкспортФон.png")
        idraw = ImageDraw.Draw(image)

        # base.execute('CREATE TABLE IF NOT EXISTS ' + str(name) + '(link, header)')
        # base.commit()
        # cur.execute('INSERT INTO ' + str(name) + ' VALUES(?, ?)', ('0', '0'))
        # base.commit()

        font = ImageFont.truetype("articulat-cf-extra-light.ttf", size=35)
        idraw.text((800, 315), message_arr[1], font=font)

        font = ImageFont.truetype("articulat-cf-demi-bold.ttf", size=20)
        PosX1 = 522
        PosX2 = 707
        PosY = 680
        count_db_table = 1
        count = 2
        while count < 17:
            info0 = cur.execute('SELECT info0 FROM line' + str(count_db_table)).fetchall()
            info1 = cur.execute('SELECT info1 FROM line' + str(count_db_table)).fetchall()
            if str(message_arr[count]) == '-':
                idraw.text((PosX1+22, PosY-10), '_', font=font, fill="#a8a8a6")  # 1 0
                idraw.text((PosX1+27, PosY-10), '_', font=font, fill="#a8a8a6")  # Для жирности
            else:
                if int(info0[0][0]) == int(message_arr[count]):
                    message_arr_output = message_arr[count][:len(message_arr[count]) - 3] + ' ' + message_arr[count][len(message_arr[count]) - 3:len(message_arr[count])]
                    idraw.rounded_rectangle((PosX1 - 7, PosY - 7, PosX1 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6", radius=7)
                    idraw.text((PosX1, PosY), message_arr_output, font=font, fill='black')  # 1 0
                elif int(info0[0][0]) < int(message_arr[count]):
                    if str(info1[0][0]) != '-':
                        message_arr_output = message_arr[count][:len(message_arr[count]) - 3] + ' ' + message_arr[count][len(message_arr[count]) - 3:len(message_arr[count])]
                        idraw.rounded_rectangle((PosX1 - 7, PosY - 15 - 7, PosX1 - 7 + 80, PosY - 15 - 7 + 31), fill="#67a947", radius=7)
                        idraw.text((PosX1, PosY - 15), message_arr_output, font=font, fill='#ffffff')  # 1 0
                        idraw.text((PosX1+1, PosY-15), message_arr_output, font=font, fill='#ffffff')  # Для жирности
                        info0output = info0[0][0][:len(info0[0][0]) - 3] + ' ' + info0[0][0][len(info0[0][0]) - 3:len(info0[0][0])]
                        idraw.text((PosX1+5, PosY + 15), info0output, font=font, fill='#ffffff')  # 1 0
                    else:
                        message_arr_output = message_arr[count][:len(message_arr[count]) - 3] + ' ' + message_arr[count][len(message_arr[count]) - 3:len(message_arr[count])]
                        idraw.rounded_rectangle((PosX1 - 7, PosY - 7, PosX1 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6", radius=7)
                        idraw.text((PosX1, PosY), message_arr_output, font=font, fill='black')  # 1 0
                elif int(info0[0][0]) > int(message_arr[count]):
                    if str(info1[0][0]) != '-':
                        message_arr_output = message_arr[count][:len(message_arr[count]) - 3] + ' ' + message_arr[count][len(message_arr[count]) - 3:len(message_arr[count])]
                        idraw.rounded_rectangle((PosX1 - 7, PosY - 15 - 7, PosX1 - 7 + 80, PosY - 15 - 7 + 31), fill="#ac4540", radius=7)
                        idraw.text((PosX1, PosY - 15), message_arr_output, font=font, fill='#ffffff')  # 1 0
                        idraw.text((PosX1+1, PosY-15), message_arr_output, font=font, fill='#ffffff')  # Для жирности
                        info0output = info0[0][0][:len(info0[0][0]) - 3] + ' ' + info0[0][0][len(info0[0][0]) - 3:len(info0[0][0])]
                        idraw.text((PosX1+5, PosY + 15), info0output, font=font, fill='#ffffff')  # 1 0
                    else:
                        message_arr_output = message_arr[count][:len(message_arr[count]) - 3] + ' ' + message_arr[count][len(message_arr[count]) - 3:len(message_arr[count])]
                        idraw.rounded_rectangle((PosX1 - 7, PosY - 7, PosX1 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6", radius=7)
                        idraw.text((PosX1, PosY), message_arr_output, font=font, fill='black')  # 1 0

            if str(message_arr[count+1]) == '-':
                idraw.text((PosX2+22, PosY-10), '_', font=font, fill="#a8a8a6")  # 0 1
                idraw.text((PosX2+27, PosY-10), '_', font=font, fill="#a8a8a6")  # Для жирности
            else:
                if int(info1[0][0]) == int(message_arr[count + 1]):
                    message_arr_output = message_arr[count+1][:len(message_arr[count+1]) - 3] + ' ' + message_arr[count+1][len(message_arr[count+1]) - 3:len(message_arr[count+1])]
                    idraw.rounded_rectangle((PosX2 - 7, PosY - 7, PosX2 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6", radius=7)
                    idraw.text((PosX2, PosY), message_arr_output, font=font, fill='black')  # 0 1
                elif int(info1[0][0]) < int(message_arr[count + 1]):
                    if str(info1[0][0]) != '-':
                        message_arr_output = message_arr[count+1][:len(message_arr[count+1]) - 3] + ' ' + message_arr[count+1][len(message_arr[count+1]) - 3:len(message_arr[count+1])]
                        idraw.rounded_rectangle((PosX2 - 7, PosY - 15 - 7, PosX2 - 7 + 80, PosY - 15 - 7 + 31), fill="#67a947", radius=7)
                        idraw.text((PosX2, PosY - 15), message_arr_output, font=font, fill='#ffffff')  # 1 0
                        idraw.text((PosX2+1, PosY-15), message_arr_output, font=font, fill='#ffffff')  # Для жирности
                        info1output = info1[0][0][:len(info1[0][0]) - 3] + ' ' + info1[0][0][len(info1[0][0]) - 3:len(info1[0][0])]
                        idraw.text((PosX2+5, PosY + 15), info1output, font=font, fill='#ffffff')  # 1 0
                    else:
                        message_arr_output = message_arr[count+1][:len(message_arr[count+1]) - 3] + ' ' + message_arr[count+1][len(message_arr[count+1]) - 3:len(message_arr[count+1])]
                        idraw.rounded_rectangle((PosX2 - 7, PosY - 7, PosX2 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6", radius=7)
                        idraw.text((PosX2, PosY), message_arr_output, font=font, fill='black')  # 0 1
                elif int(info1[0][0]) > int(message_arr[count + 1]):
                    if str(info1[0][0]) != '-':
                        message_arr_output = message_arr[count+1][:len(message_arr[count+1]) - 3] + ' ' + message_arr[count+1][len(message_arr[count+1]) - 3:len(message_arr[count+1])]
                        idraw.rounded_rectangle((PosX2 - 7, PosY - 15 - 7, PosX2 - 7 + 80, PosY - 15 - 7 + 31), fill="#ac4540", radius=7)
                        idraw.text((PosX2, PosY - 15), message_arr_output, font=font, fill='#ffffff')  # 1 0
                        idraw.text((PosX2+1, PosY-15), message_arr_output, font=font, fill='#ffffff')  # Для жирности
                        info1output = info1[0][0][:len(info1[0][0]) - 3] + ' ' + info1[0][0][len(info1[0][0]) - 3:len(info1[0][0])]
                        idraw.text((PosX2+5, PosY + 15), info1output, font=font, fill='#ffffff')  # 1 0
                    else:
                        message_arr_output = message_arr[count+1][:len(message_arr[count+1]) - 3] + ' ' + message_arr[count+1][len(message_arr[count+1]) - 3:len(message_arr[count+1])]
                        idraw.rounded_rectangle((PosX2 - 7, PosY - 7, PosX2 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6", radius=7)
                        idraw.text((PosX2, PosY), message_arr_output, font=font, fill='black')  # 0 1
            if count_db_table == 1 or count_db_table == 4 or count_db_table == 6:
                PosY += 80
            if count_db_table == 2 or count_db_table == 3 or count_db_table == 5 or count_db_table == 7:
                PosY += 85

            cur.execute('DROP TABLE line' + str(count_db_table))
            base.commit()
            base.execute('CREATE TABLE IF NOT EXISTS line' + str(count_db_table) + '(info0, info1)')
            base.commit()
            cur.execute('INSERT INTO line' + str(count_db_table) + ' VALUES(?, ?)', (message_arr[count], message_arr[count + 1]))
            base.commit()
            count_db_table += 1
            count += 2
        image = image.crop((60, 0, 1020, 1420))
        image.save('ВнутреннийРынокИтог.png')
        image0 = open('ВнутреннийРынокИтог.png', 'rb')
        await bot.send_photo(id, image0)

    # Экспорт
    if str(message_arr[0]) == 'Экспорт':
        base = sqlite3.connect('PhotoRinok.db')
        cur = base.cursor()
        image = Image.open("ВнутреннийРынокФон.png")
        idraw = ImageDraw.Draw(image)

        font = ImageFont.truetype("articulat-cf-extra-light.ttf", size=35)
        idraw.text((800, 315), message_arr[1], font=font)

        font = ImageFont.truetype("articulat-cf-demi-bold.ttf", size=20)
        PosX1 = 522
        PosX2 = 707
        PosY = 680
        count_db_table = 1
        count = 2
        while count < 17:
            info0 = cur.execute('SELECT info0 FROM line' + str(count_db_table)).fetchall()
            info1 = cur.execute('SELECT info1 FROM line' + str(count_db_table)).fetchall()
            if str(message_arr[count]) == '-':
                idraw.text((PosX1 + 22, PosY - 10), '_', font=font, fill="#a8a8a6")  # 1 0
                idraw.text((PosX1 + 27, PosY - 10), '_', font=font, fill="#a8a8a6")  # Для жирности
            else:
                if int(info0[0][0]) == int(message_arr[count]):
                    message_arr_output = message_arr[count][:len(message_arr[count]) - 3] + ' ' + message_arr[count][
                                                                                                  len(message_arr[
                                                                                                          count]) - 3:len(
                                                                                                      message_arr[
                                                                                                          count])]
                    idraw.rounded_rectangle((PosX1 - 7, PosY - 7, PosX1 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6",
                                            radius=7)
                    idraw.text((PosX1, PosY), message_arr_output, font=font, fill='black')  # 1 0
                elif int(info0[0][0]) < int(message_arr[count]):
                    if str(info1[0][0]) != '-':
                        message_arr_output = message_arr[count][:len(message_arr[count]) - 3] + ' ' + message_arr[
                                                                                                          count][len(
                            message_arr[count]) - 3:len(message_arr[count])]
                        idraw.rounded_rectangle((PosX1 - 7, PosY - 15 - 7, PosX1 - 7 + 80, PosY - 15 - 7 + 31),
                                                fill="#67a947", radius=7)
                        idraw.text((PosX1, PosY - 15), message_arr_output, font=font, fill='#ffffff')  # 1 0
                        idraw.text((PosX1 + 1, PosY - 15), message_arr_output, font=font,
                                   fill='#ffffff')  # Для жирности
                        info0output = info0[0][0][:len(info0[0][0]) - 3] + ' ' + info0[0][0][
                                                                                 len(info0[0][0]) - 3:len(info0[0][0])]
                        idraw.text((PosX1 + 5, PosY + 15), info0output, font=font, fill='#ffffff')  # 1 0
                    else:
                        message_arr_output = message_arr[count][:len(message_arr[count]) - 3] + ' ' + message_arr[
                                                                                                          count][len(
                            message_arr[count]) - 3:len(message_arr[count])]
                        idraw.rounded_rectangle((PosX1 - 7, PosY - 7, PosX1 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6",
                                                radius=7)
                        idraw.text((PosX1, PosY), message_arr_output, font=font, fill='black')  # 1 0
                elif int(info0[0][0]) > int(message_arr[count]):
                    if str(info1[0][0]) != '-':
                        message_arr_output = message_arr[count][:len(message_arr[count]) - 3] + ' ' + message_arr[
                                                                                                          count][len(
                            message_arr[count]) - 3:len(message_arr[count])]
                        idraw.rounded_rectangle((PosX1 - 7, PosY - 15 - 7, PosX1 - 7 + 80, PosY - 15 - 7 + 31),
                                                fill="#ac4540", radius=7)
                        idraw.text((PosX1, PosY - 15), message_arr_output, font=font, fill='#ffffff')  # 1 0
                        idraw.text((PosX1 + 1, PosY - 15), message_arr_output, font=font,
                                   fill='#ffffff')  # Для жирности
                        info0output = info0[0][0][:len(info0[0][0]) - 3] + ' ' + info0[0][0][
                                                                                 len(info0[0][0]) - 3:len(info0[0][0])]
                        idraw.text((PosX1 + 5, PosY + 15), info0output, font=font, fill='#ffffff')  # 1 0
                    else:
                        message_arr_output = message_arr[count][:len(message_arr[count]) - 3] + ' ' + message_arr[
                                                                                                          count][len(
                            message_arr[count]) - 3:len(message_arr[count])]
                        idraw.rounded_rectangle((PosX1 - 7, PosY - 7, PosX1 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6",
                                                radius=7)
                        idraw.text((PosX1, PosY), message_arr_output, font=font, fill='black')  # 1 0

            if str(message_arr[count + 1]) == '-':
                idraw.text((PosX2 + 22, PosY - 10), '_', font=font, fill="#a8a8a6")  # 0 1
                idraw.text((PosX2 + 27, PosY - 10), '_', font=font, fill="#a8a8a6")  # Для жирности
            else:
                if int(info1[0][0]) == int(message_arr[count + 1]):
                    message_arr_output = message_arr[count + 1][:len(message_arr[count + 1]) - 3] + ' ' + message_arr[
                                                                                                              count + 1][
                                                                                                          len(
                                                                                                              message_arr[
                                                                                                                  count + 1]) - 3:len(
                                                                                                              message_arr[
                                                                                                                  count + 1])]
                    idraw.rounded_rectangle((PosX2 - 7, PosY - 7, PosX2 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6",
                                            radius=7)
                    idraw.text((PosX2, PosY), message_arr_output, font=font, fill='black')  # 0 1
                elif int(info1[0][0]) < int(message_arr[count + 1]):
                    if str(info1[0][0]) != '-':
                        message_arr_output = message_arr[count + 1][:len(message_arr[count + 1]) - 3] + ' ' + \
                                             message_arr[count + 1][
                                             len(message_arr[count + 1]) - 3:len(message_arr[count + 1])]
                        idraw.rounded_rectangle((PosX2 - 7, PosY - 15 - 7, PosX2 - 7 + 80, PosY - 15 - 7 + 31),
                                                fill="#67a947", radius=7)
                        idraw.text((PosX2, PosY - 15), message_arr_output, font=font, fill='#ffffff')  # 1 0
                        idraw.text((PosX2 + 1, PosY - 15), message_arr_output, font=font,
                                   fill='#ffffff')  # Для жирности
                        info1output = info1[0][0][:len(info1[0][0]) - 3] + ' ' + info1[0][0][
                                                                                 len(info1[0][0]) - 3:len(info1[0][0])]
                        idraw.text((PosX2 + 5, PosY + 15), info1output, font=font, fill='#ffffff')  # 1 0
                    else:
                        message_arr_output = message_arr[count + 1][:len(message_arr[count + 1]) - 3] + ' ' + \
                                             message_arr[count + 1][
                                             len(message_arr[count + 1]) - 3:len(message_arr[count + 1])]
                        idraw.rounded_rectangle((PosX2 - 7, PosY - 7, PosX2 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6",
                                                radius=7)
                        idraw.text((PosX2, PosY), message_arr_output, font=font, fill='black')  # 0 1
                elif int(info1[0][0]) > int(message_arr[count + 1]):
                    if str(info1[0][0]) != '-':
                        message_arr_output = message_arr[count + 1][:len(message_arr[count + 1]) - 3] + ' ' + \
                                             message_arr[count + 1][
                                             len(message_arr[count + 1]) - 3:len(message_arr[count + 1])]
                        idraw.rounded_rectangle((PosX2 - 7, PosY - 15 - 7, PosX2 - 7 + 80, PosY - 15 - 7 + 31),
                                                fill="#ac4540", radius=7)
                        idraw.text((PosX2, PosY - 15), message_arr_output, font=font, fill='#ffffff')  # 1 0
                        idraw.text((PosX2 + 1, PosY - 15), message_arr_output, font=font,
                                   fill='#ffffff')  # Для жирности
                        info1output = info1[0][0][:len(info1[0][0]) - 3] + ' ' + info1[0][0][
                                                                                 len(info1[0][0]) - 3:len(info1[0][0])]
                        idraw.text((PosX2 + 5, PosY + 15), info1output, font=font, fill='#ffffff')  # 1 0
                    else:
                        message_arr_output = message_arr[count + 1][:len(message_arr[count + 1]) - 3] + ' ' + \
                                             message_arr[count + 1][
                                             len(message_arr[count + 1]) - 3:len(message_arr[count + 1])]
                        idraw.rounded_rectangle((PosX2 - 7, PosY - 7, PosX2 - 7 + 80, PosY - 7 + 31), fill="#a8a8a6",
                                                radius=7)
                        idraw.text((PosX2, PosY), message_arr_output, font=font, fill='black')  # 0 1
            if count_db_table == 1 or count_db_table == 4 or count_db_table == 6:
                PosY += 80
            if count_db_table == 2 or count_db_table == 3 or count_db_table == 5 or count_db_table == 7:
                PosY += 85

            cur.execute('DROP TABLE line' + str(count_db_table))
            base.commit()
            base.execute('CREATE TABLE IF NOT EXISTS line' + str(count_db_table) + '(info0, info1)')
            base.commit()
            cur.execute('INSERT INTO line' + str(count_db_table) + ' VALUES(?, ?)',
                        (message_arr[count], message_arr[count + 1]))
            base.commit()
            count_db_table += 1
            count += 2
        image.save('ЭкспортИтог.png')
        image0 = open('ЭкспортИтог.png', 'rb')
        await bot.send_photo(id, image0)

    # Дашборд
    if str(message_arr[0]) == 'Дашборд':
        # image = image.crop((60, 0, 1020, 1420))
        image.save('ДашбордИтог.png')
        image0 = open('ДашбордИтог.png', 'rb')
        await bot.send_photo(id, image0)

    # Карта
    if str(message_arr[0]) == 'Карта':
        image = Image.open("КартаФон.png")
        idraw = ImageDraw.Draw(image)
        font = ImageFont.truetype("articulat-cf-demi-bold.ttf", size=14)

        if str(message_arr[1]) == '-':
            idraw.text((177, 120), '_', font=font, fill='black')  # 1 0 ЦфО
        else:
            idraw.text((162, 125), message_arr[1], font=font, fill='black')  # 1 0
        if str(message_arr[2]) == '-':
            idraw.text((123, 260), '_', font=font, fill='black')  # 1 0 ЮФО
        else:
            idraw.text((108, 265), message_arr[2], font=font, fill='black')  # 1 0

        if str(message_arr[3]) == '-':
            idraw.text((637, 113), '_', font=font, fill='black')  # 0 1 ЦФО
        else:
            idraw.text((622, 118), message_arr[3], font=font, fill='black')  # 0 1
        if str(message_arr[4]) == '-':
            idraw.text((581, 252), '_', font=font, fill='black')  # 0 1 ПФО
        else:
            idraw.text((566, 257), message_arr[4], font=font, fill='black')  # 0 1

        if str(message_arr[5]) == '-':
            idraw.text((177, 553), '_', font=font, fill='black')  # 2 0 ЦФО
        else:
            idraw.text((162, 558), message_arr[5], font=font, fill='black')  # 2 0
        if str(message_arr[6]) == '-':
            idraw.text((123, 702), '_', font=font, fill='black')  # 2 0 ПФО
        else:
            idraw.text((108, 707), message_arr[6], font=font, fill='black')  # 2 0

        if str(message_arr[7]) == '-':
            idraw.text((637, 555), '_', font=font, fill='black')  # 0 2 ЦФО
        else:
            idraw.text((622, 560), message_arr[7], font=font, fill='black')  # 0 2
        if str(message_arr[8]) == '-':
            idraw.text((581, 702), '_', font=font, fill='black')  # 0 2 ПФО
        else:
            idraw.text((566, 707), message_arr[8], font=font, fill='black')  # 0 2

        if str(message_arr[9]) == '-':
            idraw.text((177, 978), '_', font=font, fill='black')  # 3 0 ЦФО
        else:
            idraw.text((162, 983), message_arr[9], font=font, fill='black')  # 3 0
        if str(message_arr[10]) == '-':
            idraw.text((123, 1124), '_', font=font, fill='black')  # 3 0 ПФО
        else:
            idraw.text((108, 1129), message_arr[10], font=font, fill='black')  # 3 0

        if str(message_arr[11]) == '-':
            idraw.text((637, 978), '_', font=font, fill='black')  # 0 3 ЦФО
        else:
            idraw.text((622, 983), message_arr[11], font=font, fill='black')  # 0 3
        if str(message_arr[12]) == '-':
            idraw.text((581, 1124), '_', font=font, fill='black')  # 0 3 ПФО
        else:
            idraw.text((566, 1129), message_arr[12], font=font, fill='black')  # 0 3

        image.save('КартаИтог.png')
        image0 = open('КартаИтог.png', 'rb')
        await bot.send_photo(id, image0)


# executor.start_polling(db, skip_updates=True)
