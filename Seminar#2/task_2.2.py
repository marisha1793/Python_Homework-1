# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи 
# оно является, то есть выведите такое число n, что φ(n)=A. Если А не является 
# числом Фибоначчи, выведите число -1.

a = int(input('Введите число А: '))
fibonachi = 0
n1 = 0
n2 = 1
count_fib = 2
while fibonachi < a:
    fibonachi = n1 + n2
    n1 = n2
    n2 = fibonachi
    count_fib += 1
    if fibonachi > a:
        count_fib = 0
if count_fib != 0:
    print('Введенное число является числом Фибоначчи по счету ', count_fib)
else:
    print('-1')


