# 3. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# V.1.0.
string_ = '1 2 3 4 5 6 8 9'
li = list(map(int,string_.split()))
print(li)
for i in range(1,len(li)-1):
    if li[i]-1 != li[i-1]:
        li.insert(i,li[i]-1)
print(li)

# V.2.0.
ch = int(input('Введите количесто число: '))
list = []
list2 = [0]
import random
for item in range(0,ch):
    list.append(random.randint(1,100))
print(list)
list2[0] = list[0]
for item in range(1,ch):
    if list2[len(list2)-1]<list[item]:
        list2.append(list[item])
print(list2)

