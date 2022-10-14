# Вычислить число π c заданной точностью d
# Пример:
#   при $d = 0.001, π = 3.141
# 


from cmath import sqrt
from math import pi
from math import factorial as fact
from decimal import Decimal as dec
# from tokenize import Double


def real_pi(value: str) -> str:
    pi_100_symbol = str(1415926535897932384626433832795028841971693993751058209749445623078164062862089986280348253421170679)
    tmp = pi_100_symbol[:value]
    return '3.' + tmp


def pi_laybnitcz(count_number: int) -> dec:
    'Pi by Labnitcza.'
    count_number = int(count_number)
    number_pi = dec(0)
    for i in range(1, count_number, 4):
        number_pi += dec(4 / i)
    for i in range(3, count_number, 4):
        number_pi -= dec(4 / i)
    return number_pi


def pi_nilakanta(count_number: int) -> dec:
    'Pi by Nilakanta.'
    # π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14)
    number_pi = 3
    list_divisors = nilakanta_divisors(count_number)
    for i in range(len(list_divisors), 2):
        number_pi += dec(4 / list_divisors[i])
    for i in range(1, len(list_divisors), 2):
        number_pi -= dec(4 / list_divisors[i])
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


def pi_chudnovsky_fact2(k: int):
    'Method by Chudnovsky with factorial'
    if k == 0: 
        # return 12 * (135191409 / (sqrt(640320 ** 3)))
        return 12 * ((-1) ** k * fact(6 * k) * (135191409 + 545140134 * k) 
                    / (fact(3 * k) * (fact(k) ** 3) * ((640320 ** 3)) ** (k + 1 / 2)))
    return 12 * ((-1) ** k * fact(6 * k) * (135191409 + 545140134 * k) 
                / (fact(3 * k) * (fact(k) ** 3) * ((640320 ** 3)) ** (k + 1 / 2))) \
                + pi_chudnovsky_fact2(k - 1)

def pi_chudnovsky_unfact(k: int):
    'Method by Chudnovsky without factorial'
    return print("It's to progress.")


def main():
    list_methods = \
    {
        '1': 'real pi, up to 100 digits',
        '2': 'module "math", up to 15 digits',
        '3': 'Laybnitcza up to 27 digits',
        '4': "Nilakanta. While don't work",
        '5': 'Chudnosky, factorial',
        '6': 'Chudnosky, unfactorial',
        '7': 'exit'
    }
    
    for item in list_methods:
        print('{}: {}'.format(item, list_methods[item]))
    
    accurancy = int(input('Enter accurancy pi (1,2,...) after the comma: '))

    choice = input('Choose a method calculate the number pi or exit from program: ')
    match choice:
        case '1':
            print(f'pi = {real_pi(accurancy)}')
        case '2':
            print("{}{}".format('pi = ', round(pi, accurancy)))
        case '3':
            print(f'pi = {round(pi_laybnitcz(int(1000000)), accurancy)}') # 1 mln
        case '4':
            number_pi = pi_nilakanta(int(input('Enter a number of iteration: ')))
            print(f'pi = {pi}')
            print(number_pi)
        case '5':
            number_pi = pi_chudnovsky_fact(int(input('Enter a number of iteration: ')))
            print(f'pi = {pi}')
            print(number_pi)
        case '6':
            number_pi = pi_chudnovsky_unfact(int(input('Enter a number of iteration: ')))
            print(f'pi = {pi}')
            print(number_pi)
        case '7':
            exit()

if __name__ == '__main__':
    main()

exit(0)

# Method Laybnicza.
# pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15)...

# print("{}{:.3f}".format('pi = ', pi))
# value = 3
# print("{}{:.valuef}".format('pi = ', pi)) # why don't work?