# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from funcs import gen_rand_list


def choice_list() -> list:
    user_choice = int(input('Choice: 1, 2 - task, 3 - user list --> '))
    match user_choice:
        case 1:
            s_list = [2, 3, 4, 5, 6]
        case 2:
            s_list = [2, 3, 5, 6]
        case 3:
            # Create a universal list:
            size_list = int(input('Enter a size of list: '))
            start_list = int(input('Enter a first number of list: '))
            stop_list = int(input('Enter a last number of list: '))
            s_list = gen_rand_list(start_list, stop_list, size_list)
    return s_list


user_list = choice_list()
middle = len(user_list) // 2
reverse_list = user_list[::-1]
result_list = []

for i in range(middle):
    result_list.append(user_list[i] * reverse_list[i])
if (len(user_list) % 2 != 0):
    result_list.append(user_list[middle])
print(f'- {user_list} => {result_list}')
