# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input('Enter a number k: '))
chain = []
for i in range(1, k + 1):
    cell = pow(((1 + 1) / k), k)
    chain.append(cell)
print(sum(chain))