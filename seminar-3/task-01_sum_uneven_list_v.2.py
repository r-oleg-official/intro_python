# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

s_list = [2, 3, 5, 9, 3]

# Universal list:
# size_list = int(input('Enter a size of list: '))
# start_list = int(input('Enter a first number of list: '))
# stop_list = int(input('Enter a last number of list: '))
# s_list = rand_list(start_list, stop_list, size_list)

uneven_list = s_list[1::2]
sum = 0
for i in uneven_list:
    sum += i
print(f'Summa numbers in unven positions of list = {sum}')
