#     Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#     Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt
import os

x_point_a = int(input('Enter X-coordinate A: '))
y_point_a = int(input('Enter Y-coordinate A: '))
x_point_b = int(input('Enter X-coordinate B: '))
y_point_b = int(input('Enter Y-coordinate B: '))
os.system('cls||clear')

length_line = round(sqrt(pow((x_point_b - x_point_a), 2) +
                         pow((y_point_b - y_point_a), 2)), 2)

print(
    f'- A ({x_point_a}, {y_point_a}); B ({x_point_b}, {y_point_b}) -> {length_line}')
