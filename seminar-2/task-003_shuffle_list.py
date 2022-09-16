

from random import randint as rint

# Idea 3.

size_list = int(input('Enter size of a list: '))
r_list = [0] * size_list
for i in range(size_list):
    r_list[i] = i
print(r_list)

exit()

# Idea #2. Create list with random index. Go into all source list and replace only elements to this list of random index.


def randomizier_shuff_index(number_index=1) -> int:
    r_list = []
    for i in range(number_index):
        r_list.append(rint(0, number_index - 1))
    return r_list


size_list = int(input('Enter size of a list: '))
s_list = randomizier_shuff_index(size_list)
print(s_list)

r_list_v2 = [size_list]
for i in range(size_list):
    print(i)
    print(type(i))
    r_list_v2[i] = i
print(r_list_v2)
r_list_v2 = set(r_list_v2)
print(r_list_v2)

exit()


def randomizier_uniq_list(size_list) -> int:
    r_list = []
    for i in range(1, size_list):
        box = rint(0, size_list)
        if box not in r_list:
            r_list[i] = box
        print(r_list[i])
        print(type(r_list[i]))
    return r_list


def shuffle_list(source_list, number_circle):
    temp = source_list[0]
    for i in range(int(number_circle)):
        for j in range(1, int(len(source_list))):
            r = rint(0, int(len(source_list)) - 1)
            source_list[j] = temp
            source_list[j] = source_list[r]
            source_list[r] = temp
    return source_list


# size_list = int(input('Enter size of a list: '))
# s_list = randomizier_uniq_list(size_list)
s_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle_list(s_list, 5)
print(s_list)
