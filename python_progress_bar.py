from math import*
from time import* 
scale=20
s,m,=1,2
print ("Начало выполнения" .center (scale // 2, "-"))
start = perf_counter()
for i in range(scale+1): 
    s=sqrt((1-sqrt(1-pow(s,2)))/2)
    m=m*2
    a = '*' * i 
    b = '.' * (scale - i)
    c = (i/scale)*100 
    dur = perf_counter() - start 
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur))
    sleep(0.1)
Pi=s*m
print ("Значение числа Пи - {}".format(Pi))
print ("\n" + "Конец выполнения" .center (scale // 2, '-'))