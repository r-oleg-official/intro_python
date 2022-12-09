# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

import os

quarter = int(input('Enter a number of quater (1 - 4): '))
os.system('cls||clear')

infinity = b'\xe2\x88\x9e'.decode('utf-8')

if quarter == 1:
    print(f'X = 0 \u00f7 {infinity}, Y = 0 \u00f7 {infinity}')
elif quarter == 2:
    print(f'X = -\u221E - 0, Y = 0 - \u221E')
elif quarter == 3:
    print(f'X = -\u221E - 0, Y = -\u221E - 0')
elif quarter == 4:
    print(f'X = 0 - \u21d2, Y = -\u221E - 0')
