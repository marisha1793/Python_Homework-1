# Формат ввода
# Вводится количество играющих, затем строки, в которых могут быть их имена. Затем вводится количество имен и сами имена детей для поиска.

# Формат вывода
# Для каждого имени выведите номер строки (счет с 1), в которой оно первый раз встретилось, или -1, если такого имени не было.
# 7
# Bessy kept the garden gate,
# And Mary kept the pantry.
# Little Betty Blue Lost her holiday shoe.
# Billy, Billy, come and play.
# Yes, my Polly, so I will.
# Little Bobby Snooks was fond of his books.
# Robert Barnes, my fellow fine, can you shoe this horse of mine?
# 4
# Mary
# Jack
# Billy
# Bobby
# 2
# -1
# 4
# 6

n = int(input('Введите количество играющих: '))
list = []

for _ in range(n):
    sentence = input()
    list.append(sentence)

m = int(input('Введите количество имен: '))

for _ in range(m):
    name = input()
    for i in range(len(list)):
        if name in list:
            print(i + 1)
            break
    else:
        print(-1)

