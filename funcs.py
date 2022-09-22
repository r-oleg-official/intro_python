import os


def check_whitespace(lines):
    '''Проверка наличия пробелов и проблем с длиной строки'''
    for lno, line in enumerate(lines):
        if "\r" in line:
            yield lno+1, "\\r in line"
        if "\t" in line:
            yield lno+1, "табуляция"
        if line[:-1].rstrip(" \t") != line[:-1]:
            yield lno+1, "пробел"
# check_whitespace() принимает один аргумент, lines, который является строками обрабатываемого файла.
# Сценарий возвращает номер строки, сокращенный как lno и line, а далее идет проверка на нежелательные символы: \r, \t, табуляции и пробелы.
# Когда встречается один из этих элементов, функция выдает текущий номер строки и сообщение для юзера.
# Переменная count lno хранит в себе номер строки, а не индекс, что позволит пользователю узнать местонахождение проблемы.


def even_items(iterable):
    '''Возврат элементов ``iterable`` когда индекс четный'''
    values = []
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            values.append(value)
        print(index)
        print(not index % 2)
    return values
# В цикле for проверяется, равен ли остаток от деления index на 2 нулю и если так, то элемент добавляется к значениям.


def even_items(iterable):
    'list comprehension'
    '''Возврат элементов ``iterable`` когда индекс четный'''
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]


def gen_simple_list(num) -> int:
    'Generator of simple numbers to list'
    begin_list = [2, 3, 5, 7]
    add_list = []
    for item in range(2, num):
        if (item % 2 != 0) and \
            (item % 3 != 0) and \
            (item % 5 != 0) and \
                (item % 7 != 0):
            add_list.append(item)
    return begin_list + add_list


def calc_simple_numbers(num) -> int:
    '''Decomposition of a number to simple numbers
        in use recursive method. Don't work'''
    # simple_list = [2, 3, 5, 7, 11, 13, 15, 17, 19]
    simple_list = gen_simple_list(num)
    factors = []
    for i in range(len(simple_list)):
        for j in simple_list:
            if (num % j == 0):
                factors.append(j)
                num /= j
                break
    return factors


def game_score():
    'Game "tic-tac-toe" is drawing to console.'
    os.system('clear')
    print('----------- ')
    for i in range(1, 4):
        print(' ' + ' | '.join([board[i, y] for y in range(1, 4)]))
        print('----------- ')


def game_win_score():
    'Game "tic-tac-toe" is drawing to console after win.'
    os.system('clear')
    print('----------- ')
    for i in range(1, 4):
        print(' ' + ' | '.join([('\033[32m'+board[i, y]+'\033[0m' if (i, y)
              in win_combination else board[i, y]) for y in range(1, 4)]))
        print('----------- ')
