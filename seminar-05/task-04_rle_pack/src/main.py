# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import pack_rle as en
import unpack_rle as de


def main():
    path_to_input = "input.txt"
    path_to_output = "output.txt"
    # path_to_input = input("Введите имя входного файла: ")
    # path_to_output = input("Введите имя выходного файла: ")
    operation = input("Что сделать с файлом (1 - сжать, 2 - распаковать): ")
    match operation:
        case '1':
            en.run(path_to_input, path_to_input + ".rle")
        case '2':
            de.run(path_to_input + ".rle", path_to_output)
        case _:
            exit(0)


if __name__ == "__main__":
    main()
