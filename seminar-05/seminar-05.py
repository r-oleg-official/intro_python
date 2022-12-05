# Пример рекурсии с лямбда ф-цией
(lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v))))(lambda f: (lambda i: 1 if (i == 0) else i * f(i - 1)))(n)


def f(a, b, c, d, e):
    return a + b + c + d + e

print(f(*[1, 2, 3, 4, 5]))


def f(a, b, c, d, e):
    return a + b + c + d + e
print(f(**{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))


def func(a_1, a_2, a_3):
    return a_1, a_2, a_3
    
args = {
    'a_1': 1,
    'a_3': 3,
    'a_2': 2
}
print(func(a_1=1, a_2=2, a_3=3))
print(func(**args))
