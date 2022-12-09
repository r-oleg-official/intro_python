from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr

expression = "-2+x^1-3*x^2+x^2+100*x^3-2*x"
x = symbols('x')
formula = parse_expr(expression.replace('^', '**'), local_dict={'x': x})
print('Формула:', formula)
for i in range(3):
    y = formula.subs(x, i)
    print(f'x={i}', f'y={y}')