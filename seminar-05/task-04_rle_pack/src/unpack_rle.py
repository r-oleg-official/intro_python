# To future.
# Protocol. <RLE-N> - pack with digits
# Protocol. <RLE-W> - unpack without digits.

import file


def unpack_not_num(li: list) -> list:
    li_res = []
    for item in li:
        line = ""
        digit = ""
        ind = 0
        for i in range(1, len(item)):
            if item[i].isdigit():
                digit += item[i]
            if not item[i].isdigit():
                line += item[ind] * int(digit)
                digit = ""
                ind = i
        li_res.append(line + "\n")
    return li_res


def run(path_in: str, path_out):
    data = file.read_file(path_in)
    file.write_file(path_out, unpack_not_num(data))
    return
