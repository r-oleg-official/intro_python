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
3:59.

