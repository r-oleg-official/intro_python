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
        degree = list(map(int, item.split('x^')))
        if len(degree) == 1:
            degree.append(0)
        members.append(tuple(degree))

    return members


def sum_polinomes(polinom_1: list, polinom_2: list) -> list:
    res_polinom = []
    if len(polinom_1) > len(polinom_2): 
        max_len = len(polinom_1)
        max_pol = polinom_1
        min_len = len(polinom_2)
        min_pol = polinom_2
    else:
        max_len = len(polinom_2)
        max_pol = polinom_2
        min_len = len(polinom_1)
        min_pol = polinom_1
    # print(f'max_len {max_len}, max_pol {max_pol} \n \
        # min_len {min_len} min_pol {min_pol}')

    max_degree = polinom_2[0][1]
    for i in range(len(polinom_1)):
        if polinom_1[i][1] > max_degree:
            max_degree = polinom_2[i][1]
    print(f'max_degree {max_degree}')

    print(max_pol[0][1])
    print(type(min_pol[0][0]))
    
    for i in range(max_degree +1):
        try:
            tmp = max_pol[i][0] + min_pol[i][0]
        except ValueError:
            res_polinom.app

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
    print(polinom_1)
    print(polinom_2)
    print()
    members_polinom_1 = parse_str(polinom_1)
    print(members_polinom_1)
    members_polinom_2 = parse_str(polinom_2)
    print(members_polinom_2)
    print()
    sum_polinomes(members_polinom_1, members_polinom_2)
    print(sum_polinomes)
    # print(members_polinom_2)
    # print(members_polinom_1[4][0])


if __name__ == "__main__":
    main()