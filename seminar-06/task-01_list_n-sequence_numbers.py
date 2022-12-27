""" Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
Пример:
Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06 """


def n_sequance(num: int) -> float:
    return (1 + 1 / num) ** num


def main():
    n = int(input('Enter a number > 0: '))
    while n < 1:
        n = int(input('Enter a number > 0: '))
    n_dic = {i: round(n_sequance(i), 2) for i in range(1, n + 1)}
    print(f'{n_dic} Сумма {sum(n_dic.values())}')


if __name__ == "__main__":
    main()
