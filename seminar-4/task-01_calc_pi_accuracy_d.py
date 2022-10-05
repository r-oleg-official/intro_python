# Вычислить число c заданной точностью d
# Пример:
#   при $d = 0.001, π = 3.141

from math import pi
import decimal as dec
# Method Leibnicza.
# pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15)...


def calc_pi_laybnitcz(count_number: int):
    number_pi = 0
    for i in range(1, count_number, 4):
        number_pi += 4 / i
    for i in range(3, count_number, 4):
        number_pi -= 4 / i
    return number_pi


def calc_pi_nilakanta(list_divisors):
    'Нилаканта. '
    # π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14)
    number_pi = 3
    # print(list_divisors)
    for i in range(len(list_divisors), 2):
        number_pi += 4 / list_divisors[i]
    for i in range(1, len(list_divisors), 2):
        number_pi -= 4 / list_divisors[i]
    return number_pi


def calc_divisor(count_number: int):
    divisor_list = []
    start_number = 2
    while start_number < count_number + 1:
        tmp = start_number
        for i in range(start_number + 1, start_number + 3):
            tmp *= i
        start_number += 2
        divisor_list.append(tmp)
    return divisor_list



# count_iteration = int(input('Enter count iterations: '))
count_iteration = 10000000 # 1 mln
my_pi = calc_pi_laybnitcz(count_iteration)
print(pi)
print(my_pi)

divisors = calc_divisor(count_iteration)
my_pi = calc_pi_nilakanta(divisors)
# print(pi)
print(my_pi)


exit()


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