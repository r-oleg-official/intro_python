def fact(num) -> int:
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)
