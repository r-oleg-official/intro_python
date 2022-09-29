# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import randint

num = int(input('Enter a number N: '))

num_list = []

for i in range(num):
    num_list.append(randint(-num, num))

user_range = input(f'Enter a range in format {1} {num}, use space: ').split()

index_start, index_end = int(user_range[0]), int(user_range[1])
user_product = 1

for i in range(index_start - 1, index_end - 1):
    user_product *= num_list[i]

print(num_list)
print(f'Product of the choiced range = {user_product}')
