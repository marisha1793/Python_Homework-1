# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

S = int(input('Введите, сколько всего журавликов сделали дети: '))
a = S / 6
b = a * 4
print(f'Петя сделал {a} журавликов, Сережа сделал {a} журавликов, Катя сделала {b} журавликов')

