# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю 
# последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

list = [int(input()) for _ in range(int(input('Введите количество элементов: ')))]
print(list)
k = int(input('Введите число: '))
list_1 = [*list[:k]]
list_2 = [*list[k:]]
new_list = list_2 + list_1
print(*new_list)