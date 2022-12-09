# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['213213', 'dsf653', 'dsf', 'fdh76']
# num = 3
# Вывод: '213213', 'dsf653'

# Ver.1.0.
def search_str (base_string, find_str):
    list_res = []
    for i in base_string:
        if find_str in i:
            list_res.append(i)
    return list_res


list_1 = ['213213', 'dsf653', 'dsf', 'fdh76']
find_str = '3'
list_res = search_str(list_1, find_str)
print(list_res)

