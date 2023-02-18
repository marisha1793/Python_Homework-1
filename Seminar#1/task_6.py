# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

students1 = int(input())
students2 = int(input())
students3 = int(input())
tables1 = students1//2 + students1 % 2
tables2 = students2//2 + students2 % 2
tables3 = students3//2 + students3 % 2
print(tables1 + tables2 + tables3)