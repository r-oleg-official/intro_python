"""# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
['efg23', '79234gefg', 'sdgs', 'g53']
Поиск'2'
['efg23', '79234gefg'] """


def sort_by_str(li: list, sub_string: str) -> list:
    res_li = []
    for i in li:
        if sub_string in i:
            res_li.append(i)
    return res_li


list_1 = ['efg23', '79234gefg', 'sdgs', 'g53']
find_string = '2'
res_list = sort_by_str(list_1, find_string)
print(res_list)
