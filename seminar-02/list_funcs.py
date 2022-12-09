from random import randint as rint


def gen_rand_list(start, stop, size):
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
