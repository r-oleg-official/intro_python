# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from funcs import gen_rand_list as r_list
from collections import deque

s_list = [2, 3, 4, 5, 6]
# s_list = [2, 3, 5, 6]

# Universal list.
# size_list = int(input('Enter a size of list: '))
# start_list = int(input('Enter a first number of list: '))
# stop_list = int(input('Enter a last number of list: '))
# s_list = r_list(start_list, stop_list, size_list)


middle = len(s_list) // 2
reverse_list = s_list[::-1]
res_list = []
for i in range(middle):
    res_list.append(s_list[i] * reverse_list[i])
if (len(s_list) % 2 != 0):
    res_list.append(s_list[middle])
print(f'- {s_list} => {res_list}')

exit(0)

# Ver.2.0
middle = len(s_list) // 2
res_list = []
i, j = 0, (len(s_list) - 1)
while i < middle:
    res_list.append(s_list[i] * s_list[j])
    i += 1
    j -= 1
if (len(s_list) % 2 != 0):
    res_list.append(s_list[middle])
print(f'- {s_list} => {res_list}')

# Ver.3.0
middle = len(s_list) // 2
tmp_list = deque(s_list[:])
res_list = []
for i in range(middle):
    res_list.append(tmp_list.popleft() * tmp_list.pop())
if (len(s_list) % 2 != 0):
    res_list.append(s_list[middle])
print(f'- {s_list} => {res_list}')
