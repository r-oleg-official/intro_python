# int, float, boolean, str, list, None
# None - уник знач-е, чтобы объявить переме-ю
# а потом по коду в дальнейшем использовать.
from sys import orig_argv


value = None # но такое скорее всего не понадобиться
a = 123     # int
b = 1.23    # float
print(a)
print(type(a))  # узнать тип переменной
print(b)
print(type(b)) 
print(value)
print(type(value))

# String
s = 'hello world'
print(s) # вывод строки
t = "hello 'world'"

# Escape-последовательности.
# \[symbol] - Escape-последовательности.
#  \' - обратный слэш, апостров - зеркалирование символа апострова'.
t = 'hello \'world' 
# \n - переход на новую строку

# Интерполяция.
print(a, b, s)
print(a, '-', b, '-', s) # добавить доп данные.
print('{} - {} - {}'.format(a, b, s)) # аналог вывод как в пред строке. Слава говорит,
# сейчас так не исп-ют.
print('{1} - {2} - {0}'.format(a, b, s)) # вывод в порядке: s, a, b.
print(f'{a} - {b} - {s}') # интерполяция.

# Логические переменные
f = True    # or False
print(f)

# Массивы. Списки. Списки заменяют массивы. 
# В Python массивов как таковых нет, а есть списки "list".
list = []   # объявление списка, пустого.
print(list) # вывод списка без заморочек
list = [1, 2, 3]
print(list)
list = ['1', '2', '3', 'hello']  # список строк
list = ['1', '2', '3', 'hello', 1, 2, 3, True]  # - это динам-я типизация, но так
# лучше не делать. Лучше в одном списке будут данные одного типа.
print(list)

list = [1, 2, 3]
# col = ['hello', 1, 2, 3] # - осторожно с пробелами, например, в начале строки.
# Ошибка: unexpected indent

# Ввод и вывод данных.
print('Enter a')
a = input()         # a = 10
print('Enter b')
b = input()         # b = 20
print(a, ' + ', b, ' = ', a + b)  # вывод будет строковый = 1020

print('Enter a')
a = int(input())         # a = 10. Тип: целочисленный
# a = float(input())     # тип: вещест-1 с плав точкой
print('Enter b')
b = int(input())         # b = 20
print(a, ' + ', b, ' = ', a + b)  # вывод будет строковый = 30

# Арифметические операции:
# +, -, *, /, % (остаток деления), //, **
# Приоритет операций:
# **, (+)(плюс в круге), (-), *, /, //, %, +, -
# () - скобки мменяют приоритет. 
a = 123
b = 321
c = a + b   # обычная сумма
print(c)
a = +123    # унарный плюс, в класс-й мат-ке и програм-ии не пишется, 
# но в прог-и может быть написан.
b = -121    # Унарный минус
c = a - b
c = a * b
c = a / b   # деление работает как для вещест-х чисел
print(c)
c = a // b  # чтобы получить деление в целых числах
print(c)
c = a % b   # остаток оот деления
print(c)
c = a ** b  # возведение в степенеь.
print(c)

# В Python техн-ки нет ограничения для хранения данных. В C# это 32/64 бита.
a = 1.3
b = 3
c = a * b   # ожидание 3.9, но...
print(c)    # 3.9000000000000004 - особен-сть хранения вещ-х чисел.
c = round(a * b) # по умол-ю, будет округление по мат-м правилам.
print(c)
a = 1.3123312223
b = 3
c = round(a * b, 5) # 5 - округление до 3-х знаков после запятой.
print(c)

# присвание
a = 3
a = a + 5
a +=5   # аналог-но предыдущему варианту
a *=5   # работает и с др. ариф операциями.

# Логические операции.
# >, >=, <, <=, ==, !=.
# not(отрицание), and (конъюкция, побитовая), or (дизъюнкция) 
# - не путать с & (И, в контексте логики), |, ^.
# Еще: is, is not, in, not in - Python's функционал.
# gen
a = 1 > 4
print(a)    # False
a = 1 < 4 and 5 > 2
print(a)    # True
a = 1 == 4
print(a)    # False
a = 1 != 4
print(a)    # True
a = 'qwe'
b = 'qwe'
print(a == b)   # True
a = [1, 2]  # список
b = [1, 2]
print(a == b)   # True. Сравнение списка поэлементно.
# Тройные и четверные неравенста.
a = 1 < 3 < 5   # 1 меньше 3 меньше 5
print(a)   # True
a = 1 < 3 < 5 < 10  # 1 меньше 3 меньше 5 меньше 10
print(a)   # True
# так можно потроллить С#-друга.
func = 1
T = 4
x = 123
print(func < T > (x)) # скобки (х) не нужны.
print(func < T > x) # False

func = 1
T = 4
x = 2
print(func < T > x) # True

f = 1 > 2 or 4 < 6  # дизъюнкция двух высказываний наз высказывание ИСТИНное, тогда
# и только тогда, когда одно из высказываний ИСТИНА.ы
print(f)    # True
f = [1, 2, 3, 4]
print(f)
print(2 in f)   # True. 2-ка содержится в списке "f".
print(not 2 in f) # False

# Проверка четности числа.
is_odd = f[0] % 2 == 0 
print(is_odd)

# Python. 0 = False. 1 = True
is_odd = not f[0] % 2 #  f[0] % 2 = 1, not - отрицание 1-цы = 0, значит False.
# is_odd = not f[0] % 2 - Python's view.
print(is_odd)

# if, if-else
# if condition:
    # operator 1
    # ...
    # operator n
# else:
    # operator n + 1
    # ...
    # operator n + m
# !!! Отступы важны.
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

# if condition1:
#     # operator
# elif condition2:
#     # operator
# elif condition3:
#     # operator
# else:
#     # operator
username = input('Enter a name: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Я так ждал вас, Марина')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)

# Circles.
# While. Отступы важны.
# while condition:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original  //=10
    print(original) # можно показать знач-е original на каждом этапе.
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)

# For
# for i in enumeration:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n
# i - переменная "счетчик", in - после ключ слова указать 
# итерируемый объект, например, список, но бывают разные.
for i in 1, 2, 3, 4, 5:
    print(i ** 2)

list = [1, 2, 3, 4, 10, 5]
for i in list:
    print(i)

r = range(10)   # выдает набор/итератор 0 - 9
for i in range:
    print(i)
for i in range(10):
    print(i)
for i in range(1, 5):   # 1 - 4, через 1-цу
    print(i)
for i in range(1, 10, 2):   # 1 - 9, приращение на 2-ку
    print(i)
# Итерируемый может может быть строкой.
for i in 'qwe - rty':
    print(i)

# Строки и некоторые базовые API для строк.
text = 'съешь ещё этих мягких французких булок'
print(len(text))                    # 39 -  кол-во символов строки
print('ещё' in text)                # True - проверка наличия подстроки в строке
print(text.isdigit())               # False - все ли символы числа?
print(text.islower())               # True - все ли символы ниж регистра
print(text.replace('ещё', 'ЕЩЁ'))   # замена подстроки в строке

for c in text:
    print(c)

# Получить встроенную справку Python.
help(text.istitle)  # text., потом см. варианты, выбрать нужный метод для изучения справки.
help(int)
help(str)

# Строки. API. Срезы.
text = 'съешь ещё этих мягких французких булок'
print(text[0])                          # с - обращение к эл-ту по индексу
print(text[1])                          # ъ
print(text[len(text)])                  # IndexError, т.к. индексация с нуля
print(text[len(text) - 1])              # к, индекс 0 - послед.
print(text[-5])                         # б, -5 - отсчет индекса с конца строки
print(text[:])                          # print(text) по умол-ю = print(text[len(text) - 1])
print(text[:2])                         # съ, значит индекс [0:2], поэтому 0 не пишется.
print(text[len(text) - 2:])             # ок
print(text[2:9])                        # ешь ещё
print(text[6:-18])                      # ещё этих мягких
print(text[0:len(text):6])              # сеикакл
print(text[::6])                        # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...

# Список - пронумерованная, изменяемая коллекция объектов произвольных(зачеркнуто) типов.
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

ran = range(1, 6)
print(type(ran))            # <class 'range'> - это не тип списка list.
numbers = list(range(1, 6)) # приведение типа range к типу list
print(numbers)  # [1, 2, 3, 4, 5]
print(type(numbers))        # <class 'list'> - это уже коллекция "список"

numbers[0] = 10
print(len(numbers)) # получить кол-во эл-тов
print(f'{len(numbers)} len')
print(numbers)  # [10, 2, 3, 4, 5]

for i in numbers:
    i *= 2 # значит положить в тек перем-ю, но не в сам список!!!
    print(i)    # [20, 4, 6, 8, 10]
print(numbers)  # [10, 2, 3, 4, 5]

# Расширенный функ-л списка.
colors = ['red', 'green', 'blue']
for e in colors:
    print(e)        # red green blue
for e in colors:
    print(e * 2)    # redred greengreen blueblue
colors.append('gray')   # добавление эл-та в конец списка
print(colors == ['red', 'green', 'blue', 'gray'])   # True
colors.remove('red')    # удалить эл-т "red"
del colors[0] # удалить эл-т с индексом 0

# Описание функции.
# def function_name(x):
#     # body line 1
#     # ...
#     # body line n
#     # optional return     # оператор return может быть добавлен.
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
# В C# указывается тип возвр-го значения. В Python ф-ция может возвращать разные типы.
arg = 1
print(f(arg))
print(type(f(arg))) # <class 'str'>
arg = 2.3
print(f(arg))       
print(type(f(arg))) # <class 'int'>
arg = 2             # указать иное значение
print(f(arg))
print(type(f(arg))) # <class 'NoneType'> - возвращено "ничего".



