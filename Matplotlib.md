## Основы Matplotlib.
### Рисунки и графикию Основная идея matplotlib.

Рисунок (Figure) - объект, основа, т.е. общее окно для всех графиков, может быть множество графиков.

Графики (axes) строятся, находятся внутри figure.

Axes - это сам график, у которого есть оси, заголовок, легенда и т.д.

> Matplotlib будет работать не только в `jupiter`, но и в др IDE, только нужно будет доп вызывать метод `show`.


Например, figure - лист тетради, а все графики (axes) будут находиться внутри нашего рисунка.

    %matplotlib inline - нужно для jupiter notebook, чтобы графики отображались в jupiter (хотя и без этого работает)

Импорт библиотек:

    import numpy as np
    import matplotlib.pyplot as plt # де-факто стандарт вызова pyplot в python

Стиль графика. Шаблоны можно найти в Интернете:

    plt.style.use('seaborn-whitegrid') 

Создание рисунка fig и 1 график на нем ax, plt.subplots(1,1,1):

    fig, ax = plt.subplots() # (nrows, ncols)

Далее можно можно вызвать этот график:

    fig

Создание рисунка из 4-х графиков в 2-е колонки и 2 ряда. Вариант 1:

    fig, axes = plt.subplots(2,2) # axes - матрица из 4-х графиков

Вывод содержимого матрицы axes:

    axes
> array([[<AxesSubplot:>, <AxesSubplot:>],
       [<AxesSubplot:>, <AxesSubplot:>]], dtype=object)

Создание рисунка из 4-х графиков в 2-е колонки и 2 ряда. Вариант 2:

    figure = plt.figure()
    # figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None)
    # num - номер рисунка, figsize - (float, float) ширина и высота в дюймах, dpi - разрешение, facecolor - цвет фона, edgecolor - цвет краев.

расчертить рисунок на 4-е части и вставить график №1 в 1-ю ячейку:

    ax1 = figure.add_subplot(2,2,1)

2-й график в 2-ю ячейку:

    ax2 = figure.add_subplot(2,2,2)

3-й график в 3-ю ячейку:

    ax3 = figure.add_subplot(2,2,3)

4-я ячейка - пустая.

Пример графика:

    fig, ax = plt.subplots()
    
    x = [-3, -2, -1, 0, 1, 2, 3]
    y = [9, 4, 1, 0, 1, 4, 9]

    ax.plot(x, y) 

> fig, ax - берем объект графика (ax) и вызываем ax. и метод plot(), в который передаем х и у.

Если график 1, то можно:

    plt.plot(x, y)

