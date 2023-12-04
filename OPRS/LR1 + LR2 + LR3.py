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


#########################################################################################
#
# Для третей лабы
#
#########################################################################################
# Загрузка данных
count0 = 0
var = 4
info_arr = []
while count0 < 3:
    data = open('info_lr3_var5_yab' + str(var) +'.txt', 'r')
    info = data.readlines()
    count = 0
    while count < len(info):
        info[count] = int(info[count][:-1])
        count += 1
    info_arr += [info]
    var += 2
    count0 += 1

# Ранжирование
info_arr_0_1 = [info_arr[0], info_arr[1]]
info_arr_1_2 = [info_arr[1], info_arr[2]]
info_arr_0_1_group = []
info_arr_1_2_group = []

for count0 in range(len(info_arr_0_1)):
    for count1 in range(len(info_arr_0_1[count0])):
        info_arr_0_1_group.append([info_arr_0_1[count0][count1], count0])
info_arr_0_1_group.sort()
for count0 in range(len(info_arr_1_2)):
    for count1 in range(len(info_arr_1_2[count0])):
        info_arr_1_2_group.append([info_arr_1_2[count0][count1], count0])
info_arr_1_2_group.sort()

rank0 = 1
rankings0 = {}
for count in range(len(info_arr_0_1_group)):
    info_arr_0_1_group[count].append(rank0)
    rank0 += 1
for count in range(len(info_arr_0_1_group)):
    if info_arr_0_1_group[count][0] not in rankings0:
        rankings0[info_arr_0_1_group[count][0]] = [info_arr_0_1_group[count][2]]
    else:
        rankings0[info_arr_0_1_group[count][0]].append(info_arr_0_1_group[count][2])
rank1 = 1
rankings1 = {}
for count in range(len(info_arr_1_2_group)):
    info_arr_1_2_group[count].append(rank1)
    rank1 += 1
for count in range(len(info_arr_1_2_group)):
    if info_arr_1_2_group[count][0] not in rankings1:
        rankings1[info_arr_1_2_group[count][0]] = [info_arr_1_2_group[count][2]]
    else:
        rankings1[info_arr_1_2_group[count][0]].append(info_arr_1_2_group[count][2])

for count in range(len(info_arr_0_1_group)):
    if len(rankings0[info_arr_0_1_group[count][0]]) > 1:
        info_arr_0_1_group[count][2] = sum(rankings0[info_arr_0_1_group[count][0]]) / len(
            rankings0[info_arr_0_1_group[count][0]])
for count in range(len(info_arr_1_2_group)):
    if len(rankings1[info_arr_1_2_group[count][0]]) > 1:
        info_arr_1_2_group[count][2] = sum(rankings1[info_arr_1_2_group[count][0]]) / len(
            rankings1[info_arr_1_2_group[count][0]])

rankSum0 = 0
rankSum1 = 0
for count in range(len(info_arr_0_1_group)):
    if info_arr_0_1_group[count][1] == 0:
        rankSum0 += info_arr_0_1_group[count][2]
    if info_arr_0_1_group[count][1] == 1:
        rankSum1 += info_arr_0_1_group[count][2]
rankSum2 = 0
rankSum3 = 0
for count in range(len(info_arr_1_2_group)):
    if info_arr_1_2_group[count][1] == 0:
        rankSum2 += info_arr_1_2_group[count][2]
    if info_arr_1_2_group[count][1] == 1:
        rankSum3 += info_arr_1_2_group[count][2]
print('Cум. ранг 1 и 2 групп: ' + str(rankSum0) + ', ' + str(rankSum1))
print('Cум. ранг 3 и 4 групп: ' + str(rankSum2) + ', ' + str(rankSum3))

u0 = rankSum0 - (len(info_arr[0]) * (len(info_arr[0]) + 1)) / 2
u1 = rankSum1 - (len(info_arr[1]) * (len(info_arr[1]) + 1)) / 2
u2 = rankSum2 - (len(info_arr[1]) * (len(info_arr[1]) + 1)) / 2
u3 = rankSum3 - (len(info_arr[2]) * (len(info_arr[2]) + 1)) / 2

Uvalue0 = min(u0, u1)
Uvalue1 = min(u2, u3)
print('Значение U для 1 и 2 выборки: ' + str(Uvalue0) + ', ' + str(Uvalue1))

mU0 = (len(info_arr[0]) * len(info_arr[1])) / 2
mU1 = (len(info_arr[1]) * len(info_arr[2])) / 2

Zvalue0 = abs((Uvalue0 - mU0) / (sqrt((len(info_arr[0]) * len(info_arr[1]) * (len(info_arr[0]) + len(info_arr[1]) + 1)) / 12)))
Zvalue1 = abs((Uvalue1 - mU1) / (sqrt((len(info_arr[1]) * len(info_arr[2]) * (len(info_arr[1]) + len(info_arr[2]) + 1)) / 12)))
print('Значение Z для 1 и 2 выборки: ' + str(Zvalue0) + ', ' + str(Zvalue1))
#########################################################################################
