# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = input('Введите трехзначное число: ')
if len(a) == 3:
    sum = int(a[0]) + int(a[1]) + int(a[2])
    print('Сумма цифр числа равна', sum)
else:
    print('Это число не трехзначное, попробуй еще раз')