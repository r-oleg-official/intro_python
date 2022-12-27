"""# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
['efg23', '79234gefg', 'sdgs', 'g53']
Поиск'2'
['efg23', '79234gefg'] """


def sort_by_str(li: list, sub_string: str) -> list:
    return [item for item in li if sub_string in item]


list_1 = ['efg23', '79234gefg', 'sdgs', 'g53']
find_string = '2'
print(sort_by_str(list_1, find_string))
