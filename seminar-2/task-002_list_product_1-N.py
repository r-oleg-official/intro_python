# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Enter a number N: '))
fact = 1
num_list = []
for i in range(1, n + 1):
    fact *= i
    num_list.append(fact)
print(num_list)
