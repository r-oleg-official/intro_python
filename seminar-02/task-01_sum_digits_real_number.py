# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 0,56 -> 11

num = float(input('Enter a number: '))
arr = str(num).split('.')
sum = 0
for i in arr:
    for j in i:
        digit = int(j)
        sum += digit % 10
print(sum)
