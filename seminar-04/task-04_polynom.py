# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def gen_rand_list(start, stop, size) -> int:
    rand_li = [0] * size
    for i in range(size):
        rand_li[i] = randint(start, stop + 1)
    return rand_li


def create_polynom(factor_li: int, degree: int, result: str) -> str:
    if degree == 0: return result
    if factor_li[degree] != 0:
        result = result + '+' + str(factor_li[degree]) + 'x^' + str(degree)
    return create_polynom(factor_li, degree - 1, result)


def save_to_txt(file: str, line: str):
    with open(file, 'w') as data:
        data.write(line)


def main():
    n = int(input('Enter a degree of:'))
    k_li = tuple(gen_rand_list(0, 100, n + 1))
    polynom = ''
    polynom = create_polynom(k_li, n, polynom)[1:]
    if k_li[0] != 0:
        polynom += '+' + str(k_li[0]) + '=0'
    save_to_txt('polynom.txt', polynom)


if __name__ == "__main__":
    main()
