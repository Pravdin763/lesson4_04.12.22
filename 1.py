# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

d = input('Введите число d: ')

d_len = len(d.split('.')[1])

i = 0

n = str(math.pi)
while i < (d_len + 2) and i < len(n):
    print(n[i], end='')
    i += 1
