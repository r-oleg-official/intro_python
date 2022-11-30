# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input('Введите N для списка -N,..., N: '))
alt_n = -n

n_list = []
for i in range(alt_n, n + 1):
    n_list.append(i)
print(n_list)

range_chain = input(f'Введите индексы элементов от {alt_n} до {n} через пробел:')
range_chain = tuple(range_chain.split(' '))

product = 1
for i in range(len(range_chain)):
    if n_list[i] != 0:
        product *= n_list[int(range_chain[i])]
print(f'Вывод: {product}')
