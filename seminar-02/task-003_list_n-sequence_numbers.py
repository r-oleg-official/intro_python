# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06


def n_sequance(num: int) -> float:
    return (1 + 1 / num) ** num


n = int(input('Enter a number "n" > 0: '))
if n == 0:
    breakpoint
else:
    n_Dic = {}
    summ = 0
    
    for i in range(1, n + 1):
        n_Dic[i] = round(n_sequance(i), 2)
    
    for v in n_Dic.values():
        summ += v
    print(f'{n_Dic} Сумма {summ}')
