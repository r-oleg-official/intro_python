# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def read_file(path: str):
    with open(path, 'r') as file:
        data = file.readline()
    return data

def parse_str(str: str) -> list:
    li = []
    start_pos = 0
    i = 0
    while i < len(str):
        if (str[i] == '+') or (str[i] == '-') or (str[i] == '='):
                
            li.append(str[start_pos:i])
            start_pos = i
        i +=1
    li[len(li) -1] += 'x^0'

    members = []
    for item in li:
        members.append(tuple(map(int, item.split('x^'))))
    return members


def format_polinom(li: list) -> list:
    for i in range(len(li) - 1):
        sub_str = li[i] + li[i + 1]
        if sub_str == '**':
            li = li[:i] + '^' + li[i + 2:]
        if sub_str == 'x+' or sub_str == 'x-':
            li = li[:i] + 'x^1' + li[i + 1:]
    return li


def main():
    path_polinom_1 = 'polinom-1.txt'
    path_polinom_2 = 'polinom-2.txt'
    polinom_1 = format_polinom(read_file(path_polinom_1))
    polinom_2 = format_polinom(read_file(path_polinom_2))
    print(polinom_1)
    print(polinom_2)
    print()
    members_polinom_1 = parse_str(polinom_1)
    print(members_polinom_1)
    print()
    members_polinom_2 = parse_str(polinom_2)
    print(members_polinom_2)
    print(members_polinom_1[4][1])


if __name__ == "__main__":
    main()