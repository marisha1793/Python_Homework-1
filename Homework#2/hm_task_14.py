# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число: '))
degrees = 2

while degrees <= n:
    degrees *=2  
    if degrees <= n: 
        print(degrees, end = ' ')


