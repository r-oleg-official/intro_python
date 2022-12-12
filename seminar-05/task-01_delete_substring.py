# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def read_file(path: str) -> list:
    with open(path, 'r') as file:
        data = file.readlines()
    return data


def write_file(path: str, line: str):
    with open(path, 'w') as file:
        file.writelines(line)


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
    path_to_source = 'source_file.txt'
    path_to_result = 'result_file.txt'
    source_string = read_file(path_to_source)
    write_file(path_to_result, delete_word_with_substring_v1(source_string[0], source_string[1]))


if __name__ == '__main__':
    main()
