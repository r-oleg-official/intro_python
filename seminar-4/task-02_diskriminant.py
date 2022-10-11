from math import *

a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))

d = pow(b, 2) - 4 * a * c

if d < 0:
    print('Действительных корней нет!')
elif d == 0:
    print(f'x = {-b / (2 * a)}')
else:
    x_1 = (-b + sqrt(d)) / (2 * a)
    x_2 = (-b - sqrt(d)) / (2 * a)
    print(f'X1 ={x_1}')
    print(f'X2 ={x_2}')