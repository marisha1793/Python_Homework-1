# 4. Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, 
# и NO в противном случае.

a = str(input('Введите целое число: '))

if len(a) == 4:
    print('YES')
else:
    print('NO')