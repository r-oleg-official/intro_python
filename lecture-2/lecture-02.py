# Функции. Работа с файлами. Множества.

# для передачи данных исп: .xml, .json

# Сначала надо связать файл с переменной, определив модификатор:
# a - открытие для добавления данных, дописывать, но не переписывать. 
# Если файл не сущ-ет, то будет создан.
# r - открытие для чтения данных. Если файл не сущ-ет - ошибка.
# w - открытие для записи данных. Запись данных, если файл не существует - будет создан.
# W+ - для записи и чтения из файла. Если файла нет - будет создан.
# r+ - для чтения и дописывать в него. Если файла нет - ошибка.
# Есть еще режимы.

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')    # допишутся 
data = open('file.txt', 'w')    # старые данные удал-ся, записываются новые.
data.writelines(colors) # разделителей не будет. Данные будут добавлены слитно.
data.close() # после окончания работы нужно закрыть файл. Во избежание утечек памяти.
# ОС скажет, что он занят каким-то процессом - невозможно удалить/изменить. 

# Если понадобиться дописывать новую порцию данных.
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.write('\nLINE 2\n') # условный аргумент "LINE 2". "\n" - конец строки, для наглядности,
# перед записью и после неё.
data.write('LINE 3\n')
data.close()

data = open('file.txt', 'a')
data.write('LINE 12\n')
data.write('LINE 13\n')
data.close() 

# След. вариант работы с файлом. В данном случае не нужно вручную вызывать data.close(),
# закрытие файла автоматически.
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

# Чтение данных из файла. 
#
path = 'file.txt'       # путь к файлу
data = open(path, 'r')  # открыть в режиме чтения.
for line in data:       # в цикле пройти построчно в файле
    print(line)         # прочесть все строки.
data.close()            # закрыть файл.

exit()  # ф-ция позволяет не выполнять остальной код в скрипте.

# Данные в файлах хранятся в текстовом формате. Чтобы исп. как числа - произвести конверт-ю.

# Функции и модули. Более глубокое изучение.

# def function_name(x):
    # body line 1
    # ...
    # body line n
    # optional return

# Создание файлов с отдельным функционалом и исп. их в других файлах.

import hello # подключение скрипта "hello.py", достаточно "hello".
print(hello.f(1))   # теперь можно вызывать ф-ции из "hello.py".
import hello as h   # можно написать такой alias "h"
print(h.f(1))       # теперь можно так вызывать ф-ции.

def new_string(symbol, count):  # принимает некоторый символ, некоторе число
    return symbol * count   # Python позволяет умножать строку на число.
print(new_string('!', 5))   # !!!!!
print(new_string('!'))      # TypeError missing 1 required ...

def new_string(symbol, count = 3):  # если в вызове  не указать число, возьмется
    return symbol * count           # по-умолчанию = 3.
print(new_string('!', 5))   # !!!!!
print(new_string('!'))      # !!!
print(new_string(4))        # 12. Python распознает тип данных в момент вызова ф-ции,
                            # если аргументом передать число, то будет умножение чисел.
# !!! Аргументов по-умолчанию может быть сколько угодно, но описываются они последними.

# Передача неогранич-го кол-ва аргументов.
def concatenatio(*params):  # для этого перед аргументом "*".
    res: str = ""       # так указ тип данных. Перем "res", тип "str"
    # res: int = ""     # Если нужно работать с числами. Указание типа необязательно.
    for item in params: # Далее это набор, т.к. в ф-ции ожидание получить строку, поэтому логика 
        res += item     # завязана на строке.
    return res          # Если передать числа, логика поломается. Здесь исп. склеивание строк.
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
print(concatenatio(1, 2, 3, 4))         # TypeError

# Рекурсия.
def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34

# Кортежи - это неизменяемые списки.
a, b = 3, 4 # множественное присваивание. a = 3, b = 4.
(a, b) = (3, 4) # это уже кортеж
a = (3, 4)  # Важно. С кортежем не нужно использовать 2-е переменные.
print(a)    # (3, 4)
print(a[0]) # 3. Обращение к опред эл-ту кортежа
print(a[-1]) # 4. По аналогии со списками - отсчет с конца.
# Кортежи могут состоять из большого кол-ва, так называемых координат.
a = (3, 1, 41, 4)
print(a[-2]) # 41
a[0] = 12   # для кортежей так не работает.

# Кортеж из одной координаты
a = (3)     # Error. Т.к. определили число (int) и не получится достучаться до 0-го эл-та.
print(a[0])
a = (3,)    # Котреж из 1-го эл-та, для этого надо поставить запятую. 
            # Но присаивание координатам по прежнему нельзя.

t = ()
print(type(t))  # tuple
t = (1, )
print(type(t))  # tuple
t = (1)
print(type(t))  # int
t = (28, 9, 1990)
print(type(t))  # tuple
colors = ['red', 'green', 'blue']
print(colors)   # ['red', 'green', 'blue']
t = tuple(colors)
print(t)  # 'red', 'green', 'blue')

t = tuple(['red', 'green', 'blue'])
print(t[0])     # red
print(t[2])     # blue
print(t[10])    # IndexError: tuple index out of range
print(t[-2])    # green
print(t[-200])  # IndexError: tuple index out of range

for e in t:     # кортежи можно перебирать циклами
    print(e)    # red green blue
t[0] = 'black'  # TypeError: 'tuple' object does not support
                # item assignment

# Распаковка кортежа.
t = tuple(['red', 'green', 'blue']) # создание списка и конвертация в кортеж
red, green, blue = t    # кортеж можно распаковать в отдельные переменные
print('r:{} g:{} b:{}'.format(red, green, blue))    # r:red g:green b:blue
# Это сложная операция, двойного преобразования: создаем список, конвертируем в кортеж, 
# кортеж распаковываем в 3-и независимых переменных и дальше работаем с ними как 
# с отдельными переменными.

# Словари -  неупорядоченные коллекции произвольных объектов с доступом по ключу.
dictionary = {} # если нужен пустой
# \ {} -  чтобы не писать код в одну строку
dictionary = \
    {
        'up': 'uprow',      # добавить пару по ключу "up" и знач-е "uprow"
        'left': 'leftrow',  # ключи слева, значения справа
        'down': 'downrow',
        'right': 'rightrow'
    }

# Просмотр всего словаря ниже:
print(dictionary)   # {'up': 'uprow', 'left': 'leftrow', 'down': 'downrow', 'right': 'rightrow'}
print(dictionary['left'])   # leftrow
# типы ключей могут отличаться.
# В списках ключ - индекс. В словаре ключ - это то, что сам определил при описании: строка 'up'; 
# число, необязательно по порядку.
dictionary['left'] = 'lleftrow' # lleftrow
print(dictionary['type'])   # KeyError: 'type'
del dictionary['left']  # удаление эл-та

# Можно получить все ключи, или значения
for k in dictionary.keys():     # Получить все ключи
    print(k)
for k in dictionary:            # Получить все ключи
    print(k)
for v in dictionary.values():   # Получить все значения
    print(v)
for v in dictionary:            # Получить все значения
    print(dictionary[v])

for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))
# up: uprow
# down: downrow
# ...

# Множества - содержат уник. эл-ты но могут быть не упорядочены.
# В Python можно создать отод сущность, которая будет организовывать хранение
# упорядоченного множества, но будут рассматриваться простые.

colors = {'red', 'green', 'blue'}
print(colors)       # {'red', 'green', 'blue'}
print(type(colors)) # <'set'>
colors.add('red')
print(colors)       # {'red', 'green', 'blue'}. Ошибок не будет и добавления не будет.
colors.add('gray')
print(colors)       # {'red', 'green', 'blue', 'gray'}
colors.remove('red')    # удаление эл-та множества
print(colors)       # {'green', 'blue', 'gray'}
colors.remove('red')# KeyError: 'red'. Если эл-ьа не существует.
colors.discard('red')   # ok. Удаление эл-та, если эл-та нет, то ошибки не будет.
print(colors)       # {'green', 'blue', 'gray'}
colors.clear()      # { }. Очистка множества.
print(colors)       # set()

# Операции с множеством: пересечение/объединение/разность/(симметрическая разность) и т.д.
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()    # c = {1, 2, 3, 5, 8}. Создать новое множ-во на основе имеющегося.
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}. Объединение множеств
i = a.intersection(b)   # i = {8, 2, 5}. Пересечение множ-в.
dl = a.difference(b)    # dl = {1, 3}
dr = b.difference(a)    # dr = {13, 21}

# Есть изменяющееся множ-во.
q = a \
    .union(b) \
        .difference(a.intersection(b))
# {1, 21, 3, 13}

# Есть неизменяемое множ-во (замороженное).
s = frozenset(a)    # методы: доб-я/измен-я и т.п. не работают.

# Больше про списки.
list1 = [1, 2, 3, 4, 5]
list2 = list1   # таким образом сделали копию
for e in list1:
    print(e)
print()
for e in list2:
    print(e)
# Game.
list1[0] = 123
list2[1] = 333
for e in list1:
    print(e)
print()
for e in list2:
    print(e)
# Значение 1-го эл-та "123" поменяется в обоих списках.
# Меняя значение в одном, поменяется в другом. Значит так копировать данные списка нельзя.

# Удаление последнего эл-та списка.
list1 = [1, 2, 3, 4, 5]
print(len(list1))   # 5
print(list1.pop())  # удаление последнего и распечатка результата.
print(list1)        # [1, 2, 3, 4]
print(list1.pop())  
print(list1)        # [1, 2, 3]
print(list1.pop())  
print(list1)        # [1, 2]
print(list1.pop(0)) # удаление конкретного эл-та с индексом "0"
print(list1)        # [2]

print(list1.insert(2, 11))  # вставка эл-та "11" в список по индексу "2"
print(list1)


