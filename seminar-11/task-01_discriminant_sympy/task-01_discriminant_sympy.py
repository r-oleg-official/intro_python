# функция f(x) = 5x^2 + 10x - 30

import sympy

a, b, c = 5, 10, 30

x = sympy.symbols('x')
print(sympy.solve(5*x**2 + 10*x - 30)) # [-1 + sqrt(7), -sqrt(7) - 1]
