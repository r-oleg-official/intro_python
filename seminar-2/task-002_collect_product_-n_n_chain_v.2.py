# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. 

n = int(input('Enter a number of cells: '))
alt_n = -n
range_chain = input(f'Enter a range of numbers throught space-key ({alt_n} - {n}):')
range_chain = range_chain.split('-')

product_chain = 1
for i in range(int(range_chain[0]), int(range_chain[1]) + 1):
    if i != 0:
        product_chain *= i

print(product_chain)
