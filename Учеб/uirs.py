import math
import requests
from PIL import Image, ImageDraw

# Константы
MaxV1 = 20
MaxV2 = 20
x0 = 2
y0 = 7
alpha0 = 0
beta0 = 0

# Кусок с вводом координат точек
count = 0
point_arr = []
while True:
    point_arr += [input('Введите координаты точки №' + str(count + 1) + ': ')]
    if len(point_arr[count].split()) > 2:
        break
    count += 1

# Кусок с расчетом углов поворота для каждой точки
count = 0
alpha_arr = []
s_arr = []
beta_arr = []
while count < int(len(point_arr)):
    if int(len(point_arr[count].split())) > 2:
        x1 = int(point_arr[count].split()[0])
        y1 = int(point_arr[count].split()[1])
        s_arr += [((x1 - x0)**2 + (y1 - y0)**2)**0.5]
        if y0 < y1 and x0 == x1:
            alpha_arr += [0]
        if y0 < y1 and x0 < x1:
            alpha_arr += [math.degrees(math.atan((x1 - x0) / (y1 - y0)))]
        if y0 == y1 and x0 < x1:
            alpha_arr += [90]
        if y0 > y1 and x0 < x1:
            alpha_arr += [90 + math.degrees(math.atan((y0 - y1) / (x1 - x0)))]
        if y0 > y1 and x0 == x1:
            alpha_arr += [180]
        if y0 > y1 and x0 > x1:
            alpha_arr += [180 + math.degrees(math.atan((x0 - x1) / (y0 - y1)))]
        if y0 == y1 and x0 > x1:
            alpha_arr += [270]
        if y0 < y1 and x0 > x1:
            alpha_arr += [270 + math.degrees(math.atan((y1 - y0) / (x0 - x1)))]
        alpha_arr += [point_arr[count].split()[2]]
        beta_arr += [alpha_arr[count] - beta0]
        beta0 = alpha_arr[count]
        print('____________________________________________')
        print('Пара точек № ' + str(count + 1))
        print('Координаты первой точки (' + str(x0) + ';' + str(y0) + ')')
        print('Координаты второй точки (' + str(x1) + ';' + str(y1) + ')')
        print('Расстояние между точками S=' + str(s_arr[count]))
        print('Угол между точками: ' + str(alpha_arr[count]))
        print('Угол поворота в первой точке: ' + str(beta_arr[count]))
        print('Угол конечной ориентации: ' + str(alpha_arr[count + 1]))
    else:
        x1 = int(point_arr[count].split()[0])
        y1 = int(point_arr[count].split()[1])
        s_arr += [((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5]
        if y0 < y1 and x0 == x1:
            alpha_arr += [0]
        if y0 < y1 and x0 < x1:
            alpha_arr += [math.degrees(math.atan((x1 - x0)/(y1 - y0)))]
        if y0 == y1 and x0 < x1:
            alpha_arr += [90]
        if y0 > y1 and x0 < x1:
            alpha_arr += [90 + math.degrees(math.atan((y0 - y1)/(x1 - x0)))]
        if y0 > y1 and x0 == x1:
            alpha_arr += [180]
        if y0 > y1 and x0 > x1:
            alpha_arr += [180 + math.degrees(math.atan((x0 - x1)/(y0 - y1)))]
        if y0 == y1 and x0 > x1:
            alpha_arr += [270]
        if y0 < y1 and x0 > x1:
            alpha_arr += [270 + math.degrees(math.atan((y1 - y0)/(x0 - x1)))]
        beta_arr += [alpha_arr[count] - beta0]
        beta0 = alpha_arr[count]
        print('____________________________________________')
        print('Пара точек № ' + str(count + 1))
        print('Координаты первой точки (' + str(x0) + ';' + str(y0) + ')')
        print('Координаты второй точки (' + str(x1) + ';' + str(y1) + ')')
        print('Расстояние между точками: ' + str(s_arr[count]))
        print('Угол между точками: ' + str(alpha_arr[count]))
        print('Угол поворота в первой точке: ' + str(beta_arr[count]))
    x0 = x1
    y0 = y1
    count += 1


# Куски для визуализации
# visual = Image.new('RGB', (1500, 1000))
# draw = ImageDraw.Draw(visual)
# # draw.line((StartX, StartY, 100, 100), fill='white', width=2)
# draw.ellipse((x0 - 25, y0 - 25, x0 + 25, y0 + 25), fill='blue')
# draw.ellipse((x0 - 30, y0 + 15, x0 - 20, y0 - 20), fill='red')
# draw.ellipse((x0 - 5, y0 - 30, x0 + 5, y0 - 20), fill='red')
# visual.show()1
