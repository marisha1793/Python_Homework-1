# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

list = []
n1 = int(input('Введите первый элемент массива: '))
dif = int(input('Введите разность: '))
amount = int(input('Введите количество элементов массива: '))

el = n1
count = 0
while count < amount:
    list.append(el)
    el += dif
    count += 1
print(list)