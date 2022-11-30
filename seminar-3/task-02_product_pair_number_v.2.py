# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from funcs import gen_rand_list


def choice_list() -> list:
    user_choice = int(input('Choice: 1 - task, 2 - user list --> '))
    match user_choice:
        case 1:
            s_list = [2, 3, 4, 5, 6]
        case 2:
            # Create a universal list:
            size_list = int(input('Enter a size of list: '))
            start_list = int(input('Enter a first number of list: '))
            stop_list = int(input('Enter a last number of list: '))
            s_list = gen_rand_list(start_list, stop_list, size_list)
    return s_list


user_list = choice_list()
middle = len(user_list) // 2
result_list = []

res_list = []
i, j = 0, (len(user_list) - 1)

while i < middle:
    res_list.append(user_list[i] * user_list[j])
    i += 1
    j -= 1
if (len(user_list) % 2 != 0):
    res_list.append(user_list[middle])
print(f'- {user_list} => {res_list}')

exit()

# Ver.3.0
middle = len(s_list) // 2
tmp_list = deque(s_list[:])
res_list = []
for i in range(middle):
    res_list.append(tmp_list.popleft() * tmp_list.pop())
if (len(s_list) % 2 != 0):
    res_list.append(s_list[middle])
print(f'- {s_list} => {res_list}')
