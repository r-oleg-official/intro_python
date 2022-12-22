#     Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#     Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
import os

x_point = int(input('Enter X-coordinate: '))
y_point = int(input('Enter Y-coordinate: '))
os.system('cls||clear')

if x_point == 0 and y_point == 0:
    exit(0)
elif x_point > 0 and y_point > 0:
    print(f'- x={x_point}; y={y_point} -> 1')
elif x_point < 0 < y_point:
    print(f'- x={x_point}; y={y_point} -> 2')
elif x_point < 0 and y_point < 0:
    print(f'- x={x_point}; y={y_point} -> 3')
else:
    print(f'- x={x_point}; y={y_point} -> 4')
