def gen_simple_numbers(num) -> int:
    "My version geerator of list a simple numbers. Don't work."
    # size = int(math.sqrt(number))
    list = [2]
    for i in range(len(list)):
        count = 0
        for j in range(3, num):
            if (j % list[i] == 0):
                count += 1
            # if (j % list[i] != 0):
                # list.append(j)
        if count == 0:
            list.append(i)
    return list


def list_simple_factors(num: int, s_list: int) -> int:
    '''Decomposition of a number to simple numbers
        in use recursive method. Don't work'''
    # size = int(math.sqrt(number)) # Calc useful length of list with a simple numbers.
    simple_numbers = [2, 3, 5, 7, 11, 13, 15, 17, 19]
    for i in simple_numbers:
        if (num % i == 0):
            s_list.append(i)
        return list_simple_factors(num / i)
