# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# V - \u2228 - or
# /\ - \2227 - and
# ¬ - \u00AC - not sign
# print('\u2228 - or, \u2227 - and, \u00AC - not sign')

xyz = [True, False]
print(f'X\t Y\t Z\t')
for i in range(2):
    for j in range(2):
        for k in range(2):
            left = not (xyz[i] or xyz[j] or xyz[k])
            right = not(xyz[i]) and (not (xyz[j])) and (not (xyz[k]))
            if left == right == True: 
                print(f'{xyz[i]}\t {xyz[j]}\t {xyz[k]}\t')
   