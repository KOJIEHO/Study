from math import sqrt


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


##########################################################################################
#
# Для второй лабы
#
##########################################################################################
# Константы
critical_lambda = 1.358

# Загрузка данных
count0 = 0
var = 4
info_arr = []
while count0 < 3:
    data = open('info_lr2_var5_yab' + str(var) +'.txt', 'r')
    info = data.readlines()
    count = 0
    while count < len(info):
        info[count] = info[count][:-1].replace(',', '.')
        count += 1
    info_arr += [info]
    var += 2
    count0 += 1

# Расчет математического ожидания
count0 = 0
Mat = []
while count0 < 3:
    M = 0
    count = 0
    while count < len(info_arr[count0]):
        M += float(info_arr[count0][count])/len(info_arr[count0])
        count += 1
    Mat += [M]
    count0 += 1
print('Математическое ожидание: ', Mat)

# Расчет дисперсии и сигмы
count0 = 0
Disp = []
StOt = []
while count0 < 3:
    D = 0
    count = 0
    while count < len(info_arr[count0]):
        D += (float(info_arr[count0][count]) - float(Mat[count0]))**2 / (len(info_arr[count0]) - 1)
        count += 1
    Disp += [D]
    StOt += [sqrt(D)]
    count0 += 1
print('Дисперсия: ', Disp)
print('Стандартное отклонение: ', StOt)

# Критерий Стьюдента
count0 = 0
t_value = []
df = []
while count0 < 2:
    t_value += [((Mat[count0] - Mat[count0 + 1]) / (sqrt(((Disp[count0] * (len(info_arr[count0]) - 1) + Disp[count0 + 1] * (len(info_arr[count0 + 1]) - 1)) / (len(info_arr[count0]) + len(info_arr[count0 + 1]) - 2)) * (1 / len(info_arr[count0]) + 1 / len(info_arr[count0 + 1])))))]
    df += [len(info_arr[count0]) + len(info_arr[count0 + 1]) - 2]
    count0 += 1
print('Значение критерия Стьюдента: ', t_value)
print('Степень свободы: ', df)
#########################################################################################








































# # Нормальное распределение Колмогорова-Смирнова
# count0 = 0
# Lambda_arr = []
# KS_statistic_arr = []
# while count0 < 3:
#     KS_statistic_max = 0
#     count = 0
#     while count < len(info_arr[count0]):
#         count_StatisticKS = abs((count + 1) / len(info_arr[count0]) - 0.5 * (1 + erf((float(info_arr[count0][count]) - float(Mat[count0])) / sqrt(2 * float(Disp[count0])))))
#         if count_StatisticKS > KS_statistic_max:
#             KS_statistic_max = count_StatisticKS
#         count += 1
#     Lambda = (6 * len(info_arr[count0]) * KS_statistic_max + 1) / (6 * sqrt(len(info_arr[count0])))
#     if Lambda <= critical_lambda:
#         print('Принимается')
#     else:
#         print('Не принимается')
#     Lambda_arr += [Lambda]
#     KS_statistic_arr += [KS_statistic_max]
#     count0 += 1
# print('Значение КС: ', KS_statistic_arr)
# print('Полученное критическое значение: ', Lambda_arr)
