# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]


def gen_simple_list(num) -> int:
    'Generator of simple numbers to list'
    begin_list = [2, 3, 5, 7]
    add_list = []
    for item in range(2, num):
        if (item % 2 != 0) and \
            (item % 3 != 0) and \
            (item % 5 != 0) and \
                (item % 7 != 0):
            add_list.append(item)
    return begin_list + add_list


def calc_simple_numbers(num) -> int:
    '''Decomposition of a number to simple numbers
        in use recursive method. Don't work'''
    # simple_list = [2, 3, 5, 7, 11, 13, 15, 17, 19]
    simple_list = gen_simple_list(num)
    factors = []
    for i in range(len(simple_list)):
        for j in simple_list:
            if (num % j == 0):
                factors.append(j)
                num /= j
                break
    return factors


number = int(input('Enter a number: '))
print(calc_simple_numbers(number))
