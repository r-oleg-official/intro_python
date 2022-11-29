# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора 
# псевдослучайных чисел.

# Ver.1.0
import time

r = str(time.time()).split('.')
print(r[1])


# Ver.2.0 Nikolay.
# minn - maxx - range random numbers
def my_random(minn, maxx):
    time.sleep(0.2)
    return int((time.time() % 1  * (maxx - minn)) + minn)
#                     0.9                  7           1


for i in range(10):
    # 10 - amount of digits
    print(my_random(1, 9), end=' ')


# Ver.3.0.
def random(a,b):
    the_set = set()
    list = []
    for i in range(a,b):
        the_set.add(str(i))
    for e in the_set:
        list.append(e)
    print(list)


random(5, 10)

# Ver.4.0 
from datetime import datetime


def get_random_number(n):
    now = datetime.now()
    random_number = now.time().second ** now.time().minute * now.time().microsecond
    return random_number % 10**n


print(get_random_number(3))

# Ver.5.0.
import time


def func (n):
    x = time.time() * (10 ** n)
    x %= 10 ** n
    return(round(x))


print(func(3))

