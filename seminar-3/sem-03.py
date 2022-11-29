def concatenatio_1(*params):
    res: str = ""
    for item in params:
        if type(item) == int: # базовый вариант сравнения, лучше не исп-ть
            print(type(item), item)
        if isinstance(item, int): # (объект, тип для сравнения), True/False
            print(type(item), item)
    return res


def concatenatio_2(*params):
    res: int = 0
    for item in params:
        res += item
    return res
# *params - кортеж, объявленный звездой

print(concatenatio_1('p', 'r', 'i', 'v', 'e', 't')) 
print(concatenatio_1('a', '*', 'd', '2', '$'))
print(concatenatio_2(1, 2, 3, 4))

# return 1, 'dsf', [42, 412] - вариант возврата ф-ции разного кол-ва переменных.
# Все что добавишь, то и вернет.

# Хранение данных в памяти.
# В питоне все ссылочное. Переменная - ссылка на участок памяти, а память условно линейная 
# из ячеек. В каждую ячейку можно что-то ложить. Здесь возникает некоторая особенность:
# изменяемые и неизменяемые типы данных. Изменяемые - сужаются, расширяются, напр., список, словари. 
# Неизменяемые - string, кортеж, числа.
a = 3
b = a
a += 4
print(b) # 3

# 
# 
# 

def concatenatio(a=[]):
    a.append(4)
    print(a)

concatenatio() 
concatenatio()
concatenatio()
concatenatio()
# [4]
# [4, 4]
# [4, 4, 4]
# [4, 4, 4, 4]


def concatenatio(a=None):
    if a is None:
        a = []
    a.append(4)
    print(a)

concatenatio() 
concatenatio()
concatenatio()
concatenatio()
# [4]
# [4]
# [4]
# [4]
# Теперь вывод будет работать правильно.
# 

# 
# : 


# M. Lutcz. Learn Python. T.1.
s = 'shruberry'
l = list(s)
print(l)
l[1] = 'c'
''.join(l)
print(l)

b = bytearray(b'spam')
print(b)
print(b.extend(b'eggs'))
print(b.decode())





def func(a_1, a_2, *args, **kwargs):
    return a_1, a_2, args, kwargs


print(func(1, 2, 3, 4, 542, 124, 'wetwet', key_1=10, key_2=30))