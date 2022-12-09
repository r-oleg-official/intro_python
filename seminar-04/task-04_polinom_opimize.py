# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def gen_rand_list(start, stop, size) -> int:
    random_list = [0] * size
    for i in range(size):
        random_list[i] = randint(start, stop + 1)
    return random_list


def create_polinom(factor_list: int, degree: int, result: str) -> str:
    if degree == 0: return result
    if factor_list[degree] != 0:
        result += f'x^{degree}+{factor_list[degree]}'
    return create_polinom(factor_list, degree - 1, result)


def save_to_file(str_line: str):
    with open('polinom.txt', 'w') as data:
        data.write(str_line)


def main():
    n = int(input('Enter a degree of:'))
    k_list = tuple(gen_rand_list(0, 100, n + 1))
    polinom = ''
    if k_list[0] != 0:
        polinom = f'{k_list[0]}{create_polinom(k_list, n, polinom)}=0'
    save_to_file(polinom)


if __name__ == "__main__":
    main()