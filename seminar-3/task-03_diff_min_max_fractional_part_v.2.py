# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

source_list = [1.1, 1.2, 3.1, 5, 10.01]
source_list = list(map(float, source_list))

# Ver.2.0. Uncorrected.
max, min = 0, 0
min, max = source_list[0], source_list[0]
for i in source_list:
    i -= i // 1
    if i < min:
        min = i
    if i > max:
        max = i
print(source_list)
print(max, min)
print(round((max - min), 3))


# Ver.3.0. By Stone.
# 1. нужна ф-ция подсчета кол-ва разрядов после запятой. Можно воспользоваться для счетчика enumerate()
# 1.2. условие num * div == int(num * div) % == 0
# 2. скорее всего num % digits - получить дробную часть
# 3. нахождение макс, мин, разницу.
