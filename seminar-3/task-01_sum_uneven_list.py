# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from funcs import gen_rand_list as r_list

s_list = [2, 3, 5, 9, 3]

# Universal list:
# size_list = int(input('Enter a size of list: '))
# start_list = int(input('Enter a first number of list: '))
# stop_list = int(input('Enter a last number of list: '))
# s_list = r_list(start_list, stop_list, size_list)

sum = 0
for i in range(1, len(s_list), 2):
    sum += s_list[i]
print(f'Summa numbers in unven positions of list = {sum}')
