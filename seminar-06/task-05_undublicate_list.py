"""Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.
[1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4] """


def main():
    source_li = [1, 1, 2, 3, 4, 5, 5]
    # s_list = list(map(int,(input('Enter a numbers in string: 1 2 3... ').split())))
    print(f'{source_li} -> {[item for item in source_li if source_li.count(item) == 1]}')


if __name__ == '__main__':
    main()
