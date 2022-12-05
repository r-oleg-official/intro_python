from pathlib import Path

# line = input('Введите A, B, C через пробел:').rsplit()
# a,b,c = map(int,input().split())

# 1. Считать строку набора чисел из файла. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел. Результат запишите в исодный файл (minn maxx).

# V.1. Find Min and Max
with open('task-01.txt', 'r') as f:
    string = f.read()
print(string)

array = string.split(' ')
min = min(array)
max = max(array)
print(f'Минимум - {min}, Максимум - {max}')
# без алгоритмизации )

# V.2. Find Min, Max and write to file.
f_path = 'task-01-2.txt'
with open(f_path, 'r') as f_nums:
    list_nums = f_nums.read().split(' ')

for i in range(len(list_nums)):
    list_nums[i] = int(list_nums[i])

minmax_list = [min(list_nums), max(list_nums)]

with open(f_path, 'a') as min_max:
    min_max.writelines(f"\n {minmax_list} ")

# V.3.
with open('task-01-2.txt', 'r') as f:
    string = f.read()
print(string)

array = string.split(' ')
min = min(array)
max = max(array)
print(f'Минимум :  {min}, Максимум :  {max}')


# V.4.
import random

with open('file_sem1_task1.txt', 'w') as f:
    for i in range(500):
        f.write(str(random.randint(1, 10000)) + '\n')
        

with open('file_sem1_task1.txt', 'r') as f:
    sp = [int(x) for x in f.readlines()]
print(min(sp), max(sp))
 


# Печать ключей
for k in dictionary.keys():
    print(k)
	
	
my_dict = {
    'key_1': 12,
    'key_2': 54,
    'key_3': {
        'key_4': [1, 2, 3]
    }
}

for key in my_dict:
    print(key)
	
	
	
my_dict = {
    'key_1': 12,
    'key_2': 54,
    'key_3': {
        'key_4': [1, 2, 3]
    }
}

a = my_dict['key_3']['key_4'][1] 

for val in my_dict.values():
    print(val)
	

my_dict = {
    'key_1': 12,
    'key_2': 54,
    'key_3': {
        'key_4': [1, 2, 3]
    }
}

for key, val in my_dict.items():
    print(dbl)
	

my_dict = {
    'key_1': 12,
    'key_2': 54,
    'key_3': {
        'key_4': [1, 2, 3]
    }
}

for val in my_dict.values():
    print(val)
	

my_dict = {
    'key_1': 12,
    'key_2': 54,
    'key_3': {
        'key_4': [1, 2, 3]
    }
}

for dbl in my_dict.items():
    print(dbl)
	
my_dict = {
    'key_1': 12,
    'key_2': 54,
    'key_3': {
        'key_4': [1, 2, 3]
    }
}

for key, val in my_dict.items():
    print(dbl)
	
	
my_dict = {
    'key_1': 12,
    'key_2': 54,
    'key_3': {
        'key_4': [1, 2, 3]
    }
}

my_dict.get('key_1', '?')
my_dict.get('key_100', '?')


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    # 1) с помощью математических формул нахождения корней квадратного уравнения
    # 2) с помощью дополнительных библиотек Python (scipy)

# V.1 .
from sympy.solvers import solve
from sympy import Symbol

def fun(a,b,c):
    x = Symbol('x')
    return solve(f'{a}*x**2+{b}*x+{c}', x)
    
print('Корни уравнения:', *fun(1, -16, 28))


# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input("Введите 1 число >> "))
b = int(input("Введите 2 число >> "))


def NOK(a,b):
    i = 2 #min(a, b)
    print('i = ', i)
    while True:
        if a%i==0 and b%i==0:
            break
        i += 1
    return i

print(NOK(a,b))
