#     Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#     Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

import os

day = int(input('Enter number of a day: '))
os.system('cls||clear')

if 0 < day < 6:
    print('-', day, '-> нет')
else:
    print('-', day, '-> да')