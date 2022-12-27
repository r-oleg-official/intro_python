""" Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на
нечётной позиции.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

from funcs import gen_rand_list


def choice_list() -> list:
    user_choice = int(input('Choice: 1 - task, 2 - user list --> '))
    match user_choice:
        case 1:
            s_list = [2, 3, 5, 9, 3]
        case 2:
            # Create a universal list:
            size_list = int(input('Enter a size of list: '))
            start_list = int(input('Enter a first number of list: '))
            stop_list = int(input('Enter a last number of list: '))
            s_list = gen_rand_list(start_list, stop_list, size_list)
    return s_list


user_list = choice_list()
uneven_elements = []

amount = 0
for i in range(1, len(user_list), 2):
    amount += user_list[i]
    uneven_elements.append(user_list[i])
print(
    f'{user_list} -> на нечётных позициях элементы {uneven_elements}. Ответ: {amount}')
