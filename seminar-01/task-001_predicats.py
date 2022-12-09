# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# V - \u2228 - or
# /\ - \2227 - and
# ¬ - \u00AC - not sign
# print('\u2228 - or, \u2227 - and, \u00AC - not sign')

# Ver.1.0.
#xyz = [True, False]
print(f'X\t Y\t Z\t')
for x in range(2):
    for y in range(2):
        for z in range(2):
            left = not(x or y or z)
            right = (not(x)) and (not(y)) and (not(z))
            if left == right: 
                print(f'{x}\t {y}\t {z}\t')

#exit()

# Ver.1.1.
print(f'X\t Y\t Z\t')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            left = not(x or y or z)
            right = (not(x)) and (not(y)) and (not(z))
            if left == right: 
                print(f'{x}\t {y}\t {z}\t')
