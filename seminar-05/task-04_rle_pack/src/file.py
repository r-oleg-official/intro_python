def read_file(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data


def write_file(path: str, li: list):
    data = "".join(li)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(data)
