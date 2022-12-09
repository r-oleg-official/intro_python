# Вычислить число π c заданной точностью d
# Пример:
#   при $d = 0.001, π = 3.141


from cmath import sqrt
from math import pi
from math import factorial as fact
from decimal import Decimal as dec


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


def main():
    list_methods = \
    {
        '1': 'real pi, up to 100 digits',
        '2': 'module "math", up to 15 digits',
        '3': 'Laybnitcza up to 27 digits',
        '4': 'exit'
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
            exit()

if __name__ == '__main__':
    main()

exit(0)
