# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -.
# Вычислите результат.
# Пример
# Ввод
# 8-5+2-1
# Вывод
# 4

string = '8-5+2-1'

def decision(string):
    dec = int(string[0])
    for i in range(2, len(string), 2):
        if string[i-1] == '+':
            dec += int(string[i])
        elif string[i-1] == '-':
            dec -= int(string[i])
    return dec
    

print(decision(string))

        

