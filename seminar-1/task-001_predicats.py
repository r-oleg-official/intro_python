# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# V - \u2228 - or
# /\ - \2227 - and
# ¬ - \u00AC - not sign
# print('\u2228 - or, \u2227 - and, \u00AC - not sign')


# def switch(sw):
#     if sw == 0:
#         return 1
#     else:
#         return 0

for i in range(2):
    x = i
    for j in range(2):
        y = j
        for k in range(2):
            z = k
            if not (x or y or z) == (not x) and (not y) and (not z):
                print(f'X={x}, Y={y}, Z={z}')
