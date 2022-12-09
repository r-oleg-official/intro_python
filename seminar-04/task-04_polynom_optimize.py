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


def create_polynom(factor_list: int, degree: int, result: str) -> str:
    if degree == 0: return result
    if factor_list[degree] != 0:
        result += f'x^{degree}+{factor_list[degree]}'
    return create_polynom(factor_list, degree - 1, result)


def save_to_file(line: str):
    with open('polynom.txt', 'w') as data:
        data.write(line)


def main():
    n = int(input('Enter a degree of:'))
    k_list = tuple(gen_rand_list(0, 100, n + 1))
    polynom = ''
    if k_list[0] != 0:
        polynom = f'{k_list[0]}{create_polynom(k_list, n, polynom)}=0'
    save_to_file(polynom)


if __name__ == "__main__":
    main()
