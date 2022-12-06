# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def read_file(path:str):
    with open(path,'r') as file:
        data = file.readline()
    return data


def format_polinom(li: list) -> list:
    for i in range(len(li) - 1):
        sub_str = li[i] + li[i + 1]
        if sub_str == '**':
            li = li[:i] + '^' + li[i + 2:]
        if (sub_str == 'x+') or (sub_str == 'x-') or (sub_str == 'x='):
            li = li[:i] + 'x^1' + li[i + 1:]
    return li


def parse_str(str: str)->list:    
    li = []
    start_pos = 0
    i = 0
    while i < len(str):
        if (str[i] == '+') or (str[i] == '-') or (str[i] == '='):            
            li.append(str[start_pos:i])
            start_pos = i
        i +=1

    li = list(filter(None, li))
    members = []
    
    for item in li:
        tmp = list(map(int, item.split('x^')))
        if len(tmp) == 1:
            tmp.append(0)
        members.append(tuple(tmp))

    return members


def find_max_degree(li_1: list, li_2: list) -> int:
    max_degree = li_1[0][1]

    for i in range(len(li_1)):
        if li_1[i][1] > max_degree: max_degree = li_1[i][1]
    
    for i in range(len(li_2)):
        if li_2[i][1] > max_degree: max_degree = li_2[i][1]
    
    return max_degree


def sum_polinomes(polinom_1: list, polinom_2: list) -> list:
    res_polinom = []
    max_degree = find_max_degree(polinom_1, polinom_2)
    

    for i in range(max_degree + 1):
        count, index = 0, 0
        for item in polinom_1:
            if i != item[1]: res_polinom.append(item)
            # print(item[1])
        # print(f'count ={count}')
        #if count == 0: res_polinom.append(tuple(polinom_1[i]))

        # for item in polinom_2:
            # if i == item[1]: count_2 += 1
        # if count_1 == 0: polinom_1 = polinom_1.append(tuple(polinom_1[i]))
        # if count_2 == 0: polinom_1 = polinom_1.append(tuple(polinom_1[i]))
        # if (count_1 == count_2 > 0): 
            # res_polinom.append(polinom_1[i][0] + polinom_2[i][0])
        

    # for i in range(max_degree + 1):
        # count = 0
        # for item in polinom_1:
            # if i == item[1]: count += 1
        # if count > 0: res_polinom.append(polinom_1[i])
        # if count == 0: polinom_1 = polinom_1.append(tuple([0, i]))

    # for i in range(max_degree + 1):
        # count = 0
        # for item in polinom_2:
            # if i == item[1]: count += 1
        # if count > 0: res_polinom.append(polinom_2[i])
        # if count == 0: polinom_2.append(tuple([0, i]))





    # for i in range(len(polinom_1)):
        # if polinom_1[i][1] > max_degree:
            # max_degree = polinom_2[i][1]
    # print(f'max_degree {max_degree}')

    # for i in range(find_max_degree(polinom_1) + 1):
        # for j in range(len(polinom_1)):
            # if polinom_1[]
# 
    # print(find_max_degree(polinom_2))
    # print(max_pol[0][1])
    # print(type(min_pol[0][0]))


    # for i in range(max_degree +1):
        # try:
            # tmp = max_pol[i][0] + min_pol[i][0]
        # except ValueError:
            # res_polinom.app

    # Version 1
    # for i in range(max_degree +1):
        # if max_pol[i][1] == i:
            # res_polinom.append(max_pol[i][0] + min_pol[i][0])
        # if min_pol[i][1] == i:
            # res_polinom.append(max_pol[i][0])
    


    # Version 2.
    # for i in range(max_len):
        # for j in range(min_len):
            # if max_pol[i][1] == min_pol[j][1]:
                # print(max_pol[0][j] + min_pol[0][j])
                # res_polinom.append(max_pol[0][j] + min_pol[0][j])
    
    return res_polinom



def main():
    path_polinom_1 = 'polinom-1.txt'
    path_polinom_2 = 'polinom-2.txt'
    polinom_1 = format_polinom(read_file(path_polinom_1))
    polinom_2 = format_polinom(read_file(path_polinom_2))
    # print(polinom_1)
    # print(polinom_2)
    # print()
    members_polinom_1 = parse_str(polinom_1)
    print(members_polinom_1)
    members_polinom_2 = parse_str(polinom_2)
    print(members_polinom_2)
    print()
    print(sum_polinomes(members_polinom_1, members_polinom_2))
    # print(members_polinom_2)
    # print(members_polinom_1[4][0])


if __name__ == "__main__":
    main()