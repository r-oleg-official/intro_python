# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


def read_file(path: str):
    with open(path, 'r') as file:
        data = file.readline()
    return data


def write_to_file(path: str, li: list):
    data = f'{li[0][1]}x^{li[0][0]}'

    for i in range(1, len(li) - 1):
        if li[i][1] > 0:
            data += f'+{li[i][1]}x^{li[i][0]}'
        if li[i][1] < 0:
            data += f'{li[i][1]}x^{li[i][0]}'

    if li[-2][1] > 0:
        data += f'+{li[-2][1]}x'
    else:
        data += f'{li[-2][1]}x'
    if li[-1][1] > 0:
        data += f'+{li[-1][1]}=0'
    else:
        data += f'{li[-1][1]}=0'

    with open(path, 'w') as file:
        file.write(data)


def write_to_file_for_Slava(path: str, li: list):
    """ Format style: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0"""
    data = f'{li[0][1]}*(x**{li[0][0]})'

    for i in range(1, len(li) - 1):
        if li[i][1] > 0:
            data += f' + {li[i][1]}*(x**{li[i][0]})'
        if li[i][1] < 0:
            data += f' {li[i][1]}*(x**{li[i][0]})'

    if li[-2][1] > 0:
        data += f' + {li[-2][1]}*x'
    else:
        data += f' {li[-2][1]}*x'
    if li[-1][1] > 0:
        data += f' + {li[-1][1]} = 0'
    else:
        data += f' {li[-1][1]} = 0'

    with open(path, 'w') as file:
        file.write(data)


def format_polynomial(li: list) -> list:
    for i in range(len(li) - 1):
        sub_str = li[i] + li[i + 1]
        if sub_str == '**':
            li = li[:i] + '^' + li[i + 2:]
        if (sub_str == 'x+') or (sub_str == 'x-') or (sub_str == 'x='):
            li = li[:i] + 'x^1' + li[i + 1:]
    return li


def parse_str(line: str) -> list:
    li = []
    start_pos = 0
    i = 0
    while i < len(line):
        if (line[i] == '+') or (line[i] == '-') or (line[i] == '='):
            li.append(line[start_pos:i])
            start_pos = i
        i += 1

    li = list(filter(None, li))
    members = []

    for item in li:
        tmp = list(map(int, item.split('x^')))
        if len(tmp) == 1:
            tmp.append(0)
        members.append(tuple(tmp))
    return members


def find_max_degree(li_1: list, li_2: list) -> int:
    max_degree = li_1[0][1]

    for i in range(len(li_1)):
        if li_1[i][1] > max_degree: max_degree = li_1[i][1]

    for i in range(len(li_2)):
        if li_2[i][1] > max_degree: max_degree = li_2[i][1]
    return max_degree


def add_lost_element(li: list, degree: int) -> list:
    full_indexes = [x for x in range(degree + 1)][::-1]
    li_indexes = []

    for item in li:
        li_indexes.append(item[1])

    for item in full_indexes:
        if item not in li_indexes: li.append(tuple([0, item]))
    return li


def sum_polynomials(li_1: list, li_2: list) -> list:
    res_polynomial = []
    max_degree = find_max_degree(li_1, li_2)
    li_1 = add_lost_element(li_1, max_degree)
    li_2 = add_lost_element(li_2, max_degree)
    for i in li_1:
        for j in li_2:
            if i[1] == j[1]:
                res_polynomial.append(tuple([i[1], i[0] + j[0]]))

    for item in res_polynomial:
        if item[1] == 0: res_polynomial.remove(item)

    res_polynomial.sort()
    res_polynomial.reverse()
    return res_polynomial


def main():
    path_polynomial1 = 'polynomial-1.txt'
    # -81x^4+30x**3-22x^2+97x+14=0
    path_polynomial2 = 'polynomial-2.txt'
    # 62x^5+97x^4+35x^3+69x^2+94x-82=0
    path_sum_polynomials = 'sum_polynomials.txt'
    polynomial1 = format_polynomial(read_file(path_polynomial1))
    polynomial2 = format_polynomial(read_file(path_polynomial2))
    members_polynomial1 = parse_str(polynomial1)
    members_polynomial2 = parse_str(polynomial2)
    sum_polynomials(members_polynomial1, members_polynomial2)
    # write_to_file(path_sum_polynomials, sum_polynomials(members_polynomial1, members_polynomial2))
    write_to_file_for_Slava(path_sum_polynomials, sum_polynomials(members_polynomial1, members_polynomial2))


if __name__ == "__main__":
    main()
