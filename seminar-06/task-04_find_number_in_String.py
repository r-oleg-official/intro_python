"""# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
['efg23', '79234gefg', 'sdgs', 'g53']
Поиск'2'
['efg23', '79234gefg'] """


def main():
    source_li = ['efg23', '79234gefg', 'sdgs', 'g53']
    sub_string = '2'
    print([item for item in source_li if sub_string in item])


if __name__ == "__main__":
    main()
