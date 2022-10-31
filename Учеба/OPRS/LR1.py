import numpy as np
from math import sqrt, erf, exp


##########################################################################################
#
# Для первой лабы
#
##########################################################################################
# Константы
critical_lambda = 1.358

# Загрузка данных
data = open('info_lr1_var5.txt', 'r')
info_arr = data.readlines()
count = 0
while count < len(info_arr):
    info_arr[count] = float(info_arr[count][:-1].replace(',', '.'))
    count += 1

# Расчет математического ожидания
Mat = 0
count = 0
while count < len(info_arr):
    Mat += float(info_arr[count])/len(info_arr)
    count += 1
print('Математическое ожидание: ', Mat)

# Расчет дисперсии и сигмы
Disp = 0
count = 0
while count < len(info_arr):
    Disp += (float(info_arr[count]) - Mat)**2 / (len(info_arr) - 1)
    count += 1
StOt = sqrt(Disp)
print('Дисперсия: ', Disp)
print('Стандартное отклонение: ', StOt)

# Нормальное распределение Колмогорова-Смирнова
KS_statistic_max = 0
count = 0
while count < len(info_arr):
    count_StatisticKS = abs((count + 1) / len(info_arr) - 0.5 * (1 + erf((float(info_arr[count]) - Mat) / sqrt(2 * Disp))))
    if count_StatisticKS > KS_statistic_max:
        KS_statistic_max = count_StatisticKS
    count += 1
print(KS_statistic_max)
Lambda = (6 * len(info_arr) * KS_statistic_max + 1) / (6 * sqrt(len(info_arr)))
if Lambda <= critical_lambda:
    print('Принимается')
else:
    print('Не принимается')
##########################################################################################
