# Ускоренная обработка данных: lambda, filter, map, zip, enumarate, List Comprehension.

# Анонимные, lambda функции.
def sum(x):
    return x + 10

def sum1(x):
    return x + 22

def sum3(x):
    return x + 242

def mult(x):
    return x ** 2

def mult2(x):
    return x ** 3

def mult4(x):
    return x ** 5

sum(mult(2))
sum1(mult2(2))
sum3(mult2(2))

# Есть какая-то функция
def f(x):
    x ** 2
# Функция имеет название, значит у неё есть тип.
print(type(f)) # <class 'function'>
g = f # Если присвоить, а не вызвать, напр. "f(2)"
print(f(1)) # None
print(g(1)) # None
# Так можно вызвать и g(), так и f().
#  А зачем вообще это нужно?
# Знаем, что функция может быть положена в переменную, получается можно через аргумент какой-то
# функции передать функцию.
def f(x):
    return x ** 2
print(f(2))

# Может получиться так, что в процессе работы нашего приложения такая функция может понадобиться
# один раз. Вопрос: как сократить подобный код?
# 5:20
# Что можно в пайтоне проделать? Посмотреть какой тип данных у ф-ции, а вовсе не какой 
# тип данных, а чем по себе является ф-ция?
# Если в type() передать имя ф-ции f():

print(type(f)) # <class 'function'>

# У ф-ции есть тип, а значит можно создать переменную типа "функция", а соответственно 
# положить в эту переменную какую-нибудь другую ф-цию.

g = f

# т.е не делается вызов ф-ции, не сохраняется результат вызова f(), сохраняется вся ф-ция целиком.
# В контексте приложения, g может быть использована как f.

print(type(f)) # <class 'function'>
print(type(g)) # <class 'function'>
print(f(4)) # 16
print(g(4)) # 16

# 6:36 
print()
# Теперь, в контексте приложения есть переменная, которая хранит в себе ссылку на ф-цию. Зачем это может потребоваться?


def calc1(x):
    return x + 10
print(calc1(10)) # 20


# Напр., надо теперь умножить на 10
def calc2(x):
    return x * 10
print(calc2(10)) # 100


# Если подобных операций будет много. То получится плодить одинаковую логику. Хотя в идеале можно 
# взять некую ф-цию calc(), которая в качестве агрумента будет принимать операцию и что-то 
# выдавать.


def math(op, x): # в качестве аргумента приходит операция и некое число.
    print(op(x)) # вызов ф-ции op() и передача её числа
math(calc2, 10) # 100
math(calc1, 10) # 20

# Можно обратить, не вызов ф-ции calc2(), а только её имя "calc2".

# Попробовать описать эту логику, но с 2-мя переменными.

print()


def sum(x, y):
    return x + y


def mylt(x, y):
    return x * y


# Опишем ф-цию, которая в качестве аргумента принимает ф-цию, а в качестве операндов принимать
# какие-то 2 аргумента:

def calc(op, a, b):
    print(op(a, b))
    return op(a, b)
# print и возврат одновременно не рекомендуется делать.


calc(mylt, 4, 5) # 20

# Перед запуском обязательно проговариваем что мы хотим получить.
# Важно! В качестве аргумента может быть целая ф-ция!

f = sum
calc(f, 4, 5) # 9

# Получается тройной проброс. 13:40
# Есть интересный механизм превратить вызов calc(f, 4, 5) в более красивый вид его название.
# "lambda".

sum = lambda x, y: x + y
calc(sum, 4, 5)

# Дальше можно пропустить создание отдельной переменной и сразу в качестве аргумента пробрасывать
# lambda.

calc(lambda x, y: x + y, 4, 5)

# Эта lambda ф-ция исп. часто.


# List Comprehension.
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)] - сложная конструкция, пока 
# не использовать на практике на самом старте - превращает код в абсолютно нечитаемую чепуху.
#  16:32.
# exp - некоторое выражение, item - элемент объекта, iterable - итерируемый объект:
# какая-нибудь последовательность, list, dictionary, range, или что-то др. 
#  А на выходе получится полноценный список.
# Пример: создать список, состоящий из четных чисел в диапазоне от 1 до 100.

list = []
for i in range(1, 101):
    if (i%2 == 0):
        list.append(i)
print(list)

# Или List Comprehension

list = [i for i in range(1, 101)]
print(list)

# Теперь, если надо добавить условие "если число четное"

list = [i for i in range(1, 101) if i % 2 == 0]
print(list)

# Создание пары чисел, кортежи. 19:14

list = [(i, i) for i in range(1, 101) if i % 2 == 0]
print(list)

# Также спокойно можно обрабатывать данные, т.е. указывать не просто само значение объекта (i, i),
# само значение аргумента "i", а взять какую-нибудь ф-цию:


def f(x):
    return x ** 3
list = [f(i) for i in range(1, 101) if i % 2 == 0]
print(list)

# for i in range(1, 101) - будут перебираться все числа от 1 до 20
# if i % 2 == 0 - из них будут выбраны только те значения, которые четные
# f(i) - и полсе этого будет к определенной выборке прим. ф-ция f(i), которая будет возводить 
# числа в степень 3.


def f(x):
    return x ** 3
list = [(i, f(i)) for i in range(1, 101) if i % 2 == 0]
print(list)

# для наглядности можно подключить кортежи, получатся пары: число и его куб (3, 9)

# А теперь, если подключить ещё лямбду-ф-цию. 20:49.
# Пример: в файле хранятся числа, нужно выбрать четные и составить список пар 
# (число; квадрат числа).
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]
path = '/home/user/file.txt'
file = open(path, 'r')
data = file.read() + ' ' # искус-но добав пробел для послед-го разреза строки
file.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos])) # срез по пробелу
    data = data[:space_pos + 1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
print(out)

# Теперь код можно сделать лучше.

def select(func, col):
    'формирование нового списка'
    return [func(x) for x in col]

def where(func, col):
    'возврат некого списка'
    return [x for x in col if func(x)]

data = '1 2 3 5 8 15 23 38'.split() # для упрощения, без файла
res = select(int, data) # сохранение рез-та в список "res", рез-ат работы ф-ции "func()", где 

# в качестве этой ф-ции, или аргумента будет передаваться ф-ция "int" -  преобразование строк
# в число, а "col" (коллекция) данных будет data.

res = where(lambda x: not x % 2, res) # 

# lambda x: not x % 2 - для проверки на четность можно описать отд ф-цию, но можно 
# описать lambda, которая будет проверять для каждого "х", возвращать рез-т для четных чисел.
# res - 2-й аргумент, рез-т на пред-м этапе.
# 32:56

res = select(lambda x: (x, x ** 2), res)
print(res) # [(2, 4), (8, 64), (38, 1444)]

# в качестве ф-ции передать lambda, принимающую "x" и возвращающую кортеж (x, x ** 2), а 2-й 
# аргумент - предыдущий рез-т "res".
# Любопытно, что описали ф-цию "select()", которая, в качестве 1-го аргумента, принимает ф-цию,
# которая отвечает за логику обработки наших данных, которые передаются 2-м аргументом. 
# И некая ф-ция "where()", которая, в качестве 1-го аргумента, принимает условия по которым 
# нужно произвести фильтр-ю объектов.

# 33:48
# А возможно в Python подобное уже есть? Это ф-ция "map()".
# Ф-ция "map()" применяет указанную ф-цию к каждому эл-ту итерируемого объекта и возвращает 
# итератор с новыми объектами.
# 
# f(x) => x + 10
# map(f, [1, 2, 3, 4, 5]) # [11, 12, 13, 14, 15]
# 
# Нельзя пройти дважды.

li = [x for x in range(1, 20)]          # [1, 2, 3, 4, 5, 6, 7, 9, 10, ..., 19]
li = map(lambda x: x + 10, li)          # получится некий объект "map"
print(li)                               # <map object at 0x7f3878f980d0>
li = list(li)                           # привести объект к типу "список"
li = list(map(lambda x: x + 10, li))    # или сразу сделать приведение к списку
print(li)                               # [11, 12, 13, 14, 15, 16, 17, 18, 19, ..., 29]

# 35:17. Ещё пример прим.-я. С клавы вводится набор чисел, числа считываются в строковом
# представлении, в качестве символа-разделителя будет пробел. Ф-ция "map()" позволяет легко 
# сделать, как в предыдущей задаче.

data = list(map(int, input().split())) # input: 2 3 4 55 6
print(data) # [2, 3, 4, 55, 6]

"""Заметка с ютуба."""
print((lambda a, b: a * b)(17, 14))         # a = 17, b = 14.
print((lambda a, b: a if a > b else b))     # сравнение на максимум.



# Приведение к типу "list" необязательно делать, а сразу пробежаться по соот-щим эл-там.

data = map(int, input().split()) # 1 2 3
for e in data:
    print(e) # 1 2 3

# Но любопытно
# 
data = map(int, '1 2 3'.split())
for e in data:
    print(e) # 1 2 3

# в итоге строка распарсилась на эл-ты и превратилась в числа. Если хочется проверить это,
# то можно доумножить.

for e in data:
    print(e * 10)   # 10 20 30

# 38:07

data = map(int, '1 2 3'.split())
for e in data:
    print(e)    # 1 2 3

print('---')
for e in data:
    print(e)    # ничего не выводится в консоль.

# map() - это некий итератор, по итератору пробежаться можно 1 раз! Поэтому если нужно дальше
# где-то с этими данными работать, то их нужно сохранить, напр. в список.
# 
# Где нужны итераторы. В частности, если большой объем данных и их все хранить и обрабатывать 
# не нужно, то можно по очереди, напр. обработать порцию данных, уйти в сон, а потом продолжить 
# через какое-то время. Или если нужно найти только какой-то один элемент, а остальные данные 
# не нужны.

# 39:23 
# Теперь можно вернуться к примеру и подправить код. Теперь ф-ция "select()" теперь не нужна.


def where(func, col):
    """возврат некого списка"""
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()     # для упрощения, без файла
res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)   # [(2, 4), (8, 64), (38, 1444)]

# 40:04. Какая ф-ция позволит избавиться от ф-ции where()? Это filter().
# Ф-ция filter() прим. указанную ф-цию к каждому эл-ту итерируемого объекта и возвращает 
# итератор с теми объектами, для которых ф-ция вернула True.
# 
# f(x) => x - четное
# filter(f, [1, 2, 3, 4, 5]) # [2, 4]
# Нельзя пройтись дважды!

data = [x for x in range(10)]
res = filter(lambda x: x % 2 == 0, data)
print(res)  # <filter object at 0x7fc0aa1f4310> - некий объект типа filter.

res = list(filter(lambda x: x % 2 == 0, data))
print(res)  # [0, 2, 4, 6, 8]


# lambda x: x % 2 == 0 - 1-й аргумент, лямбда ф-ция, проверяющая, что число четное
# data - 2-й аргумент - это набор данных.

res = list(filter(lambda x: not x % 2, data)) # условие более по-питоновски
print(res)  # [0, 2, 4, 6, 8]

# Возвращаясь к примеру, заменить ф-цию where() на filter().

data = '1 2 3 5 8 15 23 38'.split()     # для упрощения, без файла
res = map(int, data)
res = filter(lambda x: not x % 2, res) # 
res = list(map(lambda x: (x, x ** 2), res))
print(res)   # [(2, 4), (8, 64), (38, 1444)]

# Т.е. получается в Python есть все чтобы писать красивый и лаконичный код.

# 42:30.
# Ещё одна ф-ция для упрощения написания кода на Python. Это zip()
# Ф-ция zip() прим. к набору итерируемых объектов и возвращает итератор с кортежами из 
# эл-ов входных данных 
# Кол-во эл-тов в рез-те равно мин. кол-ву эл-тов входного набора.
# 
# zip ([1, 2, 3], ['о', 'д', 'т'], ['f', 's', 't'])
#     [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# 
# Нельзя пройтись дважды!
# 
# Пример. Есть набор данных user'ов и некий набор данных их id-ров:

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]

data = zip(users, ids)
print(data)     # <zip object at 0x7ff20fbf7040> - zip-объект, как и у map(), filter() собст-й тип.

data = list(zip(users, ids)) # можно привести к списку.
print(data)     # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# Если добавить список с меньшим кол-вом эл-тов:

salary = [111, 222, 333]
data = list(zip(users, ids, salary)) # можно привести к списку.
print(data)     # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# то кол-во кортежей будет по кол-ву списка "salary".

# Функция enumerate().
# Ф-ция enumerate() прим. к итерируемому объекту и возвращает новый итератор с кортежами
# из индекса и эл-тов входных данных.
# 
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#           [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3'Чикаго')]
# Нельзя пройтись дважды!
# 
# Если потребуется пронумеровать свой список можно взятьь два исходных, где данные, далее 
# какой-нибудь range(), подмешать все это в zip() и просчитать. Но есть уже готовый функционал, 
# в частности ф-ция enumerate().
# Ф-ция позволяет на вход передать какой-то набор данных, а на выходе получаются кортежи с 
# пронумерованными эл-ми.
# Пример.

users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users)) # можно привести к списку.
print(data)     # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]

# Вывод. Запомнить, что ф-цию можно пробросить через переменную - на этом базируется lambda.
