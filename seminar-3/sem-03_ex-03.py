# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# 
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1 (isinstance())
# - список: [], ищем: "123", ответ: -1


# Ver.1.0.
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
print(search_str(list_1, find_str))

list_2 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find_str = "qwe"
print(search_str(list_2, find_str))


# Ver.2.0.
def task3(sp: list, word: str) -> int:
    if word in sp:
        n1 = sp.index(word)
    else:
        return -1
    if word in sp[n1 + 1:]:
        return sp.index(word, n1 + 1)
    return -1


# Ver.2.1.
def task3(sp: list, word: str) -> int:
    if word not in sp:
        return -1
    n1 = sp.index(word)
    return sp.index(word, n1 + 1) if word in sp[n1 + 1:] else -1


# Ver.3.0.
def find_string(list: list, num):
    count = 0
    for i in range(len(list)):
        if num == list[i]:
            count +=1
            if count == 2:
                return i
    return -1
            
lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
num = input("Write string: ")

print(find_string(lst, num))