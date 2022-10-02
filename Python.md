## Переменные.

1. `int`(integer) - целочисленные;
2. `float` - числа с плавающей точкой;
3. `boolean` - логические;
4. `str`(string) - строковые;
5. `list` - списки;
6. и др.

Example:

    value = 2800
    name = 'Oleg'

Двойное присваивание:

    first_elem, second_elem = (10, "a")

## Boolean.
False = 0. True = 1.


Проверка True/False:

    print(int(False))
    print(int(True))

Ну ложь это то чего нет значит 0. Так как мы работаем с предикатами в двоичной системе счисления значит противоположность 0 будет 1. Значит 1 это истина.

### Предикаты. Алгебра Буля.
Пробел в знаниях.

## Clear console.

    import os
    os.system('cls||clear')

## If-then-else.

    if 0 < x < 10:

## Print().

    print('text', varname, '- text')
    print(f'text {varname} - text')

## String. 

### Join()

    myTuple = ("John", "Peter", "Vicky")
    x = "#".join(myTuple)
    print(x)  # John#Peter#Vicky


## Codepage [UTF-8](https://www.charset.org/utf-8).

$\infty$ - бесконечность:

    infinity = b'\xe2\x88\x9e'.decode('utf-8')
    or
    print('\u221E')

$\div$ (деление, Кроме): `\u00f7`

Copyright Sign (C): `\u00A9`. Trade Mark Sign: `\2122`. Service Mark: `\2120`

Sound Recording Copyright: `\2117`
Rightwards Double Arrow: `\u21d2`

Degree Celsius: `\u2103`. Degree Fahrenheit: `\u2109`

1. Unicode Block “Mathematical Operators”. [см](https://www.compart.com/en/unicode/block/U+2200)

2. Unicode Block “Currency Symbols”. [см](https://www.compart.com/en/unicode/category/Sc)
    
    Euro Sign: `\u20AC`;
    
    Dollar Sign: `\u0024`;
    
    Bitcoin Sign: `\u20BF`;
    
    Pound Sign: `\u00A3`.

3. Characters of Category “Math Symbol” [см](https://www.compart.com/en/unicode/category/Sm)


4. Characters with Decomposition Mapping “Vulgar fraction form” - дроби. [см](https://www.compart.com/en/unicode/decomposition/%3Cfraction%3E) 

5. List of HTML Entities [см](https://www.compart.com/en/unicode/html)


    type(var)._ _name_ _ -  возвращает строку с типом переменной.

## GUI in Python.

FM:
1. Kivi
2. PyQt
3. PyGUI
4. TKinter. Якобы пердустановлен в Python, хотя на Linux утс-ть отдельно `python3.10-tk`. Подробная док-ция. Подойдет для быстрой зарисовки проекта, красота не главное. 



## Rules in Python.
[Python с нуля | if __name__ == '__main__' | Зачем? И почему нужно использовать](https://youtu.be/houlvw937fg).

    def main():
        'Organize work of our programm'
        return requests.get(url='https://google.com')


    if __name__ == '__main__':
        'It's begin start of a project.'
        main()


Это паттерное проектрирование. Описать с начала ф-ции, а в конце описать так ф-цию `main`. Это должно облегчить чтение кода.

## Urls.
1. [Python enumerate: упрощаем циклы с помощью счетчиков](https://proglib.io/p/python-enumerate-uproshchaem-cikly-s-pomoshchyu-schetchikov-2020-12-08)
2. [Генерация простых чисел](https://habr.com/ru/post/470159/). [Таблица простых чисел до 1000](https://calcs.su/html/calcs/math/prime-numbers-1000.html)
3. [Tkinter — создание графического интерфейса в Python](https://python-scripts.com/tkinter)

