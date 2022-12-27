# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# Fn = F(n+2)−F(n+1)

def list_fibo(num: int) -> int:
    """Numbers of the Fibonacchi."""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return list_fibo(num - 1) + list_fibo(num - 2)


def list_nega_fibo(num: int) -> int:
    """Numbers of the NegaFibonacchi."""
    if num == 0:
        return 0
    if num == 1:
        return 1
    return (-1) ** (num + 1) * list_fibo(num)


number = int(input('Enter a number: '))
fib = [0]
nega_fib = []
count = 1
while count <= number:
    fib.append(list_fibo(count))
    nega_fib.append(list_nega_fibo(count))
    count += 1

print(f'Для k = {number}, список будет выглядеть так: {nega_fib[::-1] + fib}')
