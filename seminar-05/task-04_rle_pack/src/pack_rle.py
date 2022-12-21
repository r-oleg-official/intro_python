# To future.
# Protocol. <RLE-N> - pack with digits
# Protocol. <RLE-W> - unpack without digits.

import file


def check_digits(li: list):
    li_dub = li[:]
    for item in list(set("".join(li_dub))):
        if str(item).isdigit(): return True
    return False


def pack_not_num(li: list) -> list:
    li[-1] = li[-1] + "\n"
    li_res = []

    for item in li:
        count = 1
        line = ""
        for i in range(1, len(item)):
            if item[i] == item[i - 1]:
                count += 1
            if item[i] != item[i - 1]:
                line += item[i - 1] + str(count)
                count = 1
        li_res.append(line + "\n")
    return li_res


def pack_num(li: list):
    return "In progress."


def run(path_in: str, path_out):
    data = file.read_file(path_in)
    match check_digits(data):
        case True:
            print(pack_num(data))
        case False:
            result = pack_not_num(data)
            file.write_file(path_out, result)
    return
