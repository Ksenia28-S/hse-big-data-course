#!/usr/bin/env python

import sys

# создаем список [длина, среднее, дисперсия]
res = [0, 0, 0]



# обрабатываем строки
for line in sys.stdin:
    line = line.replace('\n', '').split(' ')
    line = [float(i) for i in line]

    # считаем новые среднее и дисперсию
    mean_new = (res[0]*res[1] + line[0]*line[1]) / (res[0] + line[0])
    var_new = (res[0]*res[2] + line[0]*line[2]) / (res[0] + line[0]) + res[0] * line[0] * ((res[1] - line[1]) / (res[0] + line[0]))**2
    res[0] = res[0] + line[0]
    res[1] = mean_new
    res[2] = var_new

print (res[1], res[2])
