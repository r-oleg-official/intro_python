# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def dec_to_bin(num: int) -> str:
    'Convert integer number to binary.'
    if num == 0:
        return 0
    bin = ""
    while (num > 0):
        if (num % 2 == 0):
            bin = "0" + bin
        else:
            bin = "1" + bin
        num = num // 2
    return bin


number = int(input('Enter a number: '))
print(f'- {number} => {dec_to_bin(number)}')
