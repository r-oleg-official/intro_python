# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


def check_dublicate(s_list, number) -> bool:
    count = 0
    for i in range(1, len(s_list)):
        if s_list[i] == number:
            return True
    return False

def main():
    s_list = [1, 1, 2, 3, 4, 5, 5]
    # s_list = list(map(int,(input('Enter a numbers in string: 1 2 3... ').split())))
    res_list = []
    # res_list = s_list[:]
    i = 0
    while i < len(s_list):
        # res_list = []
        tmp = s_list[i]
        j = 0
        while j < len(s_list):
            if res_list[j] == tmp: 
                res_list.append(s_list[j])
            j += 1
        # res_list.append(s_list[i])
        i += 1
    print(res_list)
# print(main())

if __name__ == '__main__':
    main()