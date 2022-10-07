# Вычислить число π c заданной точностью d
# Пример:
#   при $d = 0.001, π = 3.141
# 
# Method Laybnicza.
# pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15)...


from cmath import sqrt
from math import pi
from math import factorial as fact
from decimal import *


def pi_laybnitcz(count_number: int) -> Decimal:
    'Pi by Labnitcza.'
    count_number = int(count_number)
    number_pi = Decimal(0)
    for i in range(1, count_number, 4):
        number_pi += Decimal(4 / i)
    for i in range(3, count_number, 4):
        number_pi -= Decimal(4 / i)
    return number_pi


def pi_nilakanta(count_number: int) -> Decimal:
    'Pi by Nilakanta.'
    # π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14)
    number_pi = 3
    list_divisors = nilakanta_divisors(count_number)
    print(len(list_divisors))
    for i in range(len(list_divisors), 2):
        number_pi += Decimal(4 / list_divisors[i])
    for i in range(1, len(list_divisors), 2):
        number_pi -= Decimal(4 / list_divisors[i])
    return number_pi


def nilakanta_divisors(count_number: int) -> list:
    'Divisors for method by Nikolanta.'
    divisor_list = []
    start_number = 2
    while start_number < count_number + 1:
        tmp = start_number
        for i in range(start_number + 1, start_number + 3):
            tmp *= i
        start_number += 2
        divisor_list.append(tmp)
    return divisor_list


def pi_chudnovsky_fact(k: int):
    'Method by Chudnovsky with factorial'
    if k == 0: 
        # return 12 * (135191409 / (sqrt(640320 ** 3)))
        return 12 * ((-1) ** k * fact(6 * k) * (135191409 + 545140134 * k) 
                    / (fact(3 * k) * (fact(k) ** 3) * ((640320 ** 3)) ** (k + 1 / 2)))
    return 12 * ((-1) ** k * fact(6 * k) * (135191409 + 545140134 * k) 
                / (fact(3 * k) * (fact(k) ** 3) * ((640320 ** 3)) ** (k + 1 / 2))) \
                + pi_chudnovsky_fact(k - 1)


def pi_chudnovsky_unfact(k: int):
    'Method by Chudnovsky without factorial'
    return print("It's to progress.")


# count_iteration = int(input('Enter count iterations: '))
# count_iteration = 10000000 # 10 mln
# count_iteration = 1000000 # 1 mln
# count_iteration = 100000 # 100 thousand
# count_iteration = 10000 # 10 thousand
# count_iteration = 1000 # 1 thousand
# print(f'module "math": {Decimal(pi)}')
# my_pi = calc_pi_laybnitcz(count_iteration)
# print(f'Laybnitcza:    {my_pi}')
# my_pi = calc_pi_nilakanta(count_iteration)
# print(f'Nilakanta: {my_pi}')
# my_pi = pi_chudnovsky(count_iteration)
# print(f'pi by Chudnovsky: {pi_chudnovsky(count_iteration)}')

# print(f'pi by Chudnovsky: {pi_chudnovsky(17)}')


def main():
    list_methods = \
    {
        '1': 'module "math"',
        '2': 'Laybnitcza',
        '3': 'Nilakanta',
        '4': 'Chudnosky, factorial',
        '5': 'Chudnosky, unfactorial',
        '6': 'real pi',
        '7': 'exit'
    }
    
    for item in list_methods:
        print('{}: {}'.format(item, list_methods[item]))
    
    choice = input('Choose a method calculate the number pi or exit from program: ')
    match choice:
        case '1':
            print(pi)
        case '2':
            number_pi = pi_laybnitcz(int(input('Enter a number of iteration: ')))
            print(pi)
            print(number_pi)
        case '3':
            number_pi = pi_nilakanta(int(input('Enter a number of iteration: ')))
            print(pi)
            print(number_pi)
        case '4':
            number_pi = pi_chudnovsky_fact(int(input('Enter a number of iteration: ')))
            print(pi)
            print(number_pi)
        case '5':
            number_pi = pi_chudnovsky_unfact(int(input('Enter a number of iteration: ')))
            print(pi)
            print(number_pi)
        case '6':
            print('pi = 3.1415926535897932384626433832795028841971693993751058209749445623078164062862089986280348253421170679')
        case '7':
            exit()

if __name__ == '__main__':
    main()

exit(0)


# def calc_list(count_number: int = 20):
    # list_numbers = []
    # for i in range(1, count_number * 2, 2):
        # list_numbers.append(4 / i)
    # return list_numbers
# 
# 
# for i in range(3, (count_iteration * 2 - 1), 2):
    # if switch == True:
        # number_pi -= (4 / i)
        # switch = False
    # else: number_pi += (4 / i)


# count_iteration = int(input('Enter count iterations: '))
# switch = True
# number_pi = 4
# print(pi)
# print(number_pi)



# x = 9876
# pi = 2 * (Arcsin(sqrt (1 - x ^ 2))) + abs(Arcsin (х))
# 
# 
d = int(input('Enter accuracy d: '))
# x = 9876
# pi = x * sin(180/x)
# print(pi)