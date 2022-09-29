# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

def k_seq(num) -> float:
    return (1 + 1 / num) ** num


k = int(input('Enter a number "k" > 0: '))
if k == 0:
    breakpoint
else:
    k_list = []
    for i in range(1, k + 1):
        k_list.append(k_seq(i))
    print(k_list)
