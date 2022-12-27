""" Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на
нечётной позиции.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

from random import randint


def main():
    user_choice = int(input('Choice: 1 - task, 2 - user list --> '))
    match user_choice:
        case 1:
            user_list = [2, 3, 5, 9, 3]
        case 2:
            # Create a universal random list by user's size:
            size_list = int(input('Enter a size of list: '))
            start_list = int(input('Enter a first number of list: '))
            stop_list = int(input('Enter a last number of list: '))
            user_list = [randint(start_list, stop_list + 1) for item in range(size_list)]
    uneven_elements = user_list[1::2]
    print(
        f'{user_list} -> на нечётных позициях элементы {uneven_elements}. Ответ: {sum(uneven_elements)}')


if __name__ == "__main__":
    main()
