# 3. Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


def search_str (base_string, find_str):
    res_index = 0
    count = 0
    for i in range(len(base_string)):
        if find_str == base_string[i]:
            res_index = i
            count += 1
    if count <= 1:
        res_index = -1 
    return res_index


list_1 = ["123", "234", 123, "567"]
find_str = "123"

list_res = search_str(list_1, find_str)

print(list_res)
