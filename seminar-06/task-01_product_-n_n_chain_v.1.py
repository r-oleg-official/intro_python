# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input('Введите N для списка -N,..., N: '))
n_list = [i for i in range(-n, n + 1)]
print(n_list)
user_range = list(map(int, input(f'Введите индексы элементов через пробел --> ').split(" ")))
res_list = [n_list[i] for i in user_range]

prod = 1
for item in res_list:
    prod *= item
print(f'{" * ".join(map(str, res_list))}\nВывод: {prod}')
