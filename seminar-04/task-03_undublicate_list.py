# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


def list_counter_number(check_list, number):
    count = 0
    for i in check_list:
        if i == number: count += 1
    return count


def main():
    s_list = [1, 1, 2, 3, 4, 5, 5]
    # s_list = list(map(int,(input('Enter a numbers in string: 1 2 3... ').split())))
    res_list = s_list[:]
    count = 0
    for i in range(len(s_list)):
        for j in s_list:
            if j == s_list[i]: count += 1
        if list_counter_number(s_list, s_list[i]) > 1: res_list.remove(s_list[i])
    print(res_list)


if __name__ == '__main__':
    main()
