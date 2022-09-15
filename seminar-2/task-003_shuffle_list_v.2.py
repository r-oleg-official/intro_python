# Реализуйте алгоритм перемешивания списка.

from random import randint as rint


def generate_random_list(start, stop, size):
    random_list = [0] * size
    for i in range(size):
        random_list[i] = rint(start, stop + 1)
    return random_list


def shuff_list(source_list) -> int:
    for i in range(len(source_list)):
        shuff_index = rint(0, len(source_list) - 1)
        temp = source_list[shuff_index]
        source_list[shuff_index] = source_list[i]
        source_list[i] = temp
    return source_list


size_list = int(input('Enter size of a list: '))
begin_number = int(input('Enter a first number of list: '))
end_number = int(input('Enter a last number of list: '))
start_list = list(range(size_list))
start_list = generate_random_list(begin_number, end_number, size_list)
print(start_list)
result_list = shuff_list(start_list)
print(result_list)


exit()


def randomizier_shuff_index(number_index=1) -> int:
    s_list = []
    for i in range(number_index):
        s_list.append(rint(0, number_index - 1))
    print(s_list)
    return s_list


def shuff_list(source_list) -> int:
    shuff_index = randomizier_shuff_index(len(source_list))
    print(shuff_index)
    res_list = [0] * len(source_list)
    for i in range(len(source_list)):
        res_list[i] = source_list[shuff_index]
    print(res_list)
    return res_list


size_list = int(input('Enter size of a list: '))
start_list = list(range(size_list))
# print(start_list)
result_list = shuff_list(start_list)
# print(result_list)
