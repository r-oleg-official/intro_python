# 2. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 4 5 7 8 9

# V.1.0.
string_ = '1 2 3 4 5 6 8 9'
li = set(map(int, string_.split()))
li_1 = set(i for i in range(1, len(li)+1))
dif = li_1-li
print(*dif)

# V.2.0.
li = [-1, 0, 8, 5, 4, 8, 0, 12]
my_li = [li[0]]
for i in range(1, len(li)):
    if my_li[-1] < li[i]:
        my_li.append(li[i])
print(my_li)

# V.2.1.
li = [-1, 0, 8, 5, 4, 8, 0, 12]
my_li = [li[0]]
[my_li.append(li[i]) for i in range(1, len(li)) if my_li[-1] < li[i]]
print(my_li)