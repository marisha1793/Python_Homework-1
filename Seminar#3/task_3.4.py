# 23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента с предыдущим номером)

list = [int(input()) for _ in range(int(input('Введите количество элементов: ')))]
count = 0
for i in range(0, len(list) - 1):
    if list[i+1] > list[i]:
        count += 1
print(count)