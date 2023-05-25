import math
from math import sqrt
import numpy as np
import random
from matplotlib import pyplot as plt

P_list = []
I_list = []
L = 0

f = open('Cities.txt', 'r')
cities_xy = []
for line in f:
    cities_xy.append(line[2:-1].split(' '))
L = len(cities_xy)
print(f"координаты городов: {cities_xy}\n\n\n")




def dis_matrix_create():
    '''Функция создает список пар координат
    после чего возвращает матрицу расстояний'''


    move = 1000000


    dis_matrix = np.full((len(cities_xy), len(cities_xy)), 0)
    i_city = 0
    i_city_2 = 0
    for city in cities_xy:
        i_city_2 = 0
        for city_2 in cities_xy:
            x1 = float(city[0].replace(',', '.')) + move
            y1 = float(city[1].replace(',', '.')) + move
            x2 = float(city_2[0].replace(',', '.')) + move
            y2 = float(city_2[1].replace(',', '.')) + move

            L = sqrt((abs(x2 - x1) ** 2) + (abs(y2 - y1) ** 2))

            dis_matrix[i_city][i_city_2] = L

            i_city_2 += 1

        i_city += 1


    print( 'матрица расстояний\n', dis_matrix)
    return dis_matrix


def random_way():
    '''возвращает рандомный начальный путь'''
    S = []
    x = 0
    while len(S) != L:
        x = random.randint(0, L - 1)
        if x not in S:
         S.append(x)
    print(f"\n\nНачальный путь\n", S)
    return S

def new_way(S):
    '''меняем местами 2 города в пути
    и получаем новый путь'''
    S1 = S[:]
    r_ind = random.randint(0, L - 1)
    r_ind2 = random.randint(0, L - 1)
    S1[r_ind], S1[r_ind2] = S1[r_ind2], S1[r_ind]

    return S1

def lengh_way(way):
    '''Получает путь и возвращает длину этого пути'''
    L = 0
    for i in range(len(way) - 1):
        city_1 = way[i]
        city_2 = way[i + 1]
        L += dis_matrix[city_1][city_2]

    return L

dis_matrix = dis_matrix_create()

WayBegin = random_way()
WayOpt =  WayBegin
WayNew = new_way(WayBegin)
i = 0
T0 = 100
T = T0
L_opt = lengh_way(WayBegin)
L_new = lengh_way(WayNew)
Tmin = 0.001
a = 0.99999


f = open('Cities.txt', 'r')
xy = []
for line in f:
    xy.append(line[2:-1].split(' '))

x1 = []
y1 = []
for city in WayOpt:
    x1.append(float(xy[city][0].replace(',','.')))
    y1.append(float(xy[city][1].replace(',','.')))

fig, ax = plt.subplots()
plt.title(f"total path length at the first iteration  {L_opt}")
ax.plot(x1, y1, 'ro', label='cities')
ax.plot(x1, y1, label='way')

plt.grid()
ax.legend()
plt.show()


while T > Tmin:

    if L_new < L_opt:
        WayOpt = WayNew[:]
        L_opt = L_new
    else:
        p = 100 * math.e ** (-(L_new - L_opt) / T)
        P_list.append(p)
        I_list.append(i)
        if p > random.randint(0, 100):
            WayOpt = WayNew[:]
            L_opt = L_new




    WayNew = new_way(WayOpt)
    L_new = lengh_way(WayNew)
    T = T * a
    i += 1





f = open('Cities.txt', 'r')
xy = []
for line in f:
    xy.append(line[2:-1].split(' '))


x1 = []
y1 = []
for city in WayOpt:
    x1.append(float(xy[city][0].replace(',','.')))
    y1.append(float(xy[city][1].replace(',','.')))

fig, ax = plt.subplots()
plt.title(f"total path length at the last iteration  {L_opt}")
ax.plot(x1, y1, 'ro', label='cities')
ax.plot(x1, y1, label='way')

plt.grid()
ax.legend()
plt.show()

print('\n\n ', i)

