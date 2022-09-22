# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# s_list = [1.1, 1.2, 3.1, 5, 10.01]
s_list = [1.1, 1.2, 3.1, 10.01]

s_list = list(map(float, s_list))
# min, max = s_list[0], s_list[0] # - don't work
min, max = 0.02, 0.02
min, max = 1, 1
print(max, min)
for i in s_list:
    tmp = float("0." + str(i).split(".").pop())
    print(tmp)
    if tmp > max:
        max = tmp
    elif tmp < min:
        min = tmp
print(max, min)
print(f'{s_list} => {max - min}')
