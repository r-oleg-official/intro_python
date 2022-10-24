# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from random import randint


def gen_rand_list(start, stop, size) -> int:
    random_list = [0] * size
    for i in range(size):
        random_list[i] = randint(start, stop + 1)
    return random_list


def create_polinom(factor_list: int, degree: int, result: str) -> str:
    if degree == 0: return result
    if factor_list[degree] != 0:
        result = result + '+' + str(factor_list[degree]) + 'x^' + str(degree)
    return create_polinom(factor_list, degree - 1, result)


def save_to_txt(file: str, str_line: str):
    with open(file, 'w') as data:
        data.write(str_line)





def main():
    x = 1

if __name__ == "__main__":
    main()