# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def read_file(path: str) -> list:
    with open(path, 'r') as file:
        data = file.readlines()
    return data


def delete_word_with_substring_v1(line: str, sub_str: str) -> str:
    li = line.split()
    li_res = li[:]
    for item in li:
        if sub_str in item:
            li_res.remove(item)
    return " ".join(li_res)


def delete_word_with_substring_v2(line: str, sub_str: str) -> str:
    li = line.split()
    li_res = li.copy()
    sub_len = len(sub_str)
    for item in li:
        if len(item) >= sub_len:
            for i in range(len(item)):
                if sub_str[0] == item[i]:
                    tmp = item[i:i + len(sub_str)]
                    if tmp == sub_str:
                        li_res.remove(item)
    return " ".join(li_res)


def main():
    source_string = 'Я люблю абвЖвау иабв Питон'
    delete_string = 'абв'
    print('v.1', delete_word_with_substring_v1(source_string, delete_string))
    print('v.2', delete_word_with_substring_v2(source_string, delete_string))
    path_to_file = 'source_file.txt'
    source_string = read_file(path_to_file)
    print(source_string)
    print('v.1', delete_word_with_substring_v1(source_string[0], source_string[1]))


if __name__ == '__main__':
    main()
