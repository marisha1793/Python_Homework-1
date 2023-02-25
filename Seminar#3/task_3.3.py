# 21. Напишите программу для печати всех уникальных значений в словаре.

new_dict = {1:10, 2:20, 3:30, 2:20}
a = new_dict.values()
new_set = set(a)
print(new_set)






# import time

# some_list = []
# count = 0
# for _ in range(10 ** 6):
#     some_list.append(count)
#     count += 1

# some_set = set()
# count = 0
# for _ in range(10 ** 6):
#     some_set.add(count)
#     count += 1


# find_number = 999998
# start = time.perf_counter()
# print(find_number in some_list)
# end = time.perf_counter()
# a = end - start

# start = time.perf_counter()
# print(find_number in some_set)
# end = time.perf_counter()
# b = end - start
# print(a / b)