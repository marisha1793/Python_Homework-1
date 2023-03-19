# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file), которая записывает в файл 
# result.txt слово, имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, "r") as text:
        words = text.read().split()
        max = words[0]
        for i in words:
            if len(i) > len(max):
                max = i
        print(max)

longest_words('D:\\GeekBrains\\8. Знакомство с языком PYTHON\\Семинары\\СЕМИНАРЫ_PYTHON\\Homework#8\\article.txt')

