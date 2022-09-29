# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора 
# псевдослучайных чисел.

import time

r = str(time.time()).split('.')
print(r[1])

# Version 2. Nikolay.
def my_random(minn, maxx):
    time.sleep(0.3)
    return int((time.time() % 1  * (maxx - minn)) + minn)
#                     0.9                  7           1

for i in range(10):
    print(my_random(1, 9))

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
