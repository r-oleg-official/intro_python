# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# V - \u2228 - or
# /\ - \2227 - and
# ¬ - \u00AC - not sign
# print('\u2228 - or, \u2227 - and, \u00AC - not sign')


def checkPredicates(startNumber: int, endNumber: int):
    for i in range(startNumber, endNumber + 1):
        x = i
        for j in range(startNumber, endNumber + 1):
            y = j
            for k in range(startNumber, endNumber + 1):
                z = k
                if not(x or y or z) == (not (x) and not (y) and not (z)):
                    # print(f'X= {x}, Y= {y}, Z= {z}')
                    print(f'{x}\t {y}\t {z}\t')


def main():
    startNumber = int(input('Введите начальное значение для X, Y, Z: '))
    endNumber = int(input('Введите конечное значение для X, Y, Z: '))
    print(f"X \tY \tZ")
    checkPredicates(startNumber, endNumber)


if __name__ == "__main__":
    main()
