# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами 
# или началом или концом строки. Выведите все слова из строки в столбик. НЕЛЬЗЯ 
# ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)
# Формат ввода
# Вводится строка.
# Формат вывода
# Выведите слова из строки по одному.
# Пример 1
# Ввод
# Hello, world!
# Вывод
# Hello,
# world!
# Пример 2
# Ввод
# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland

sentence = input('Введите предложение: ')

def sencol(sentence):
    word = ''
    for i in range(len(sentence)+1):
        if i == len(sentence):
            return word
        elif sentence[i] != ' ':
            word += sentence[i]
        elif sentence[i] == ' ':
            word += '\n'

new_s = sencol(sentence)
print(new_s)    
