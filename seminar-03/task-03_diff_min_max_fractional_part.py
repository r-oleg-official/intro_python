# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

source_list = [1.1, 1.2, 3.1, 10.01]
source_list = list(map(float, source_list))

# min, max = s_list[0], s_list[0] # - don't work
min, max = 0.1, 0

for i in source_list:
    tmp = float("0." + str(i).split(".").pop())
    if tmp > max:
        max = tmp
    elif tmp < min:
        min = tmp
print(f'{source_list} => {max - min}')
