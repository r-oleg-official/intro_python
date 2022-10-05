# Вычислить число c заданной точностью d
# Пример:
#   при $d = 0.001, π = 3.141

from math import pi
# Method Leibnicza.
# pi = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15)...


def calc_pi_laybnitcz(count_number: int):
    number_pi = 0
    for i in range(1, count_number, 4):
        number_pi += 4 / i
    for i in range(3, count_number, 4):
        number_pi -= 4 / i
    return number_pi


# count_iteration = int(input('Enter count iterations: '))
count_iteration = 10000000000000000 # 1 mln
my_pi = calc_pi_laybnitcz(count_iteration)
print(pi)
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