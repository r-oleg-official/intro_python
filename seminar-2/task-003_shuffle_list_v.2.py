# Реализуйте алгоритм перемешивания списка.

import list_funcs as l_func


def choice_type_list():
    quest = int(input('Choice type list: 1 or 2, (default 1: [1, 2,...,n]): '))
    if quest == 1:
        return list(range(size_list))
    else:
        begin_number = int(input('Enter a first number of list: '))
        end_number = int(input('Enter a last number of list: '))
        return l_func.gen_rand_list(begin_number, end_number, size_list)


size_list = int(input('Enter size of a list: '))
my_list = choice_type_list()
print(my_list)
l_func.shuff_list(my_list)
print(my_list)
