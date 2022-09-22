from random import randint as rint


def gen_rand_list(start, stop, size):
    'Generate a random list.'
    random_list = [0] * size
    for i in range(size):
        random_list[i] = rint(start, stop + 1)
    return random_list


def shuff_list(source_list) -> int:
    'Shuffle list.'
    for i in range(len(source_list)):
        shuff_index = rint(0, len(source_list) - 1)
        temp = source_list[shuff_index]
        source_list[shuff_index] = source_list[i]
        source_list[i] = temp
    return source_list


def dec_to_bin(num: int) -> str:
    'Convert integer number to binary.'
    if num == 0:
        return 0
    bin = ""
    while (num > 0):
        if (num % 2 == 0):
            bin = "0" + bin
        else:
            bin = "1" + bin
        num = num // 2
    return bin
