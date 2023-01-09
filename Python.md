## Переменные.

1. `int`(integer) - целочисленные;
2. `float` - числа с плавающей точкой;
3. `boolean` - логические;
4. `str`(string) - строковые;
5. `list` - списки;
6. и др.
7. `decimal` [см](https://docs.python.org/3.10/library/decimal.html): <br>

    `from decimal import *`

    `number = Decimal(number)`


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

## Venv of Python.
### VSCode on Linux.
Терминал VSC:

    $ python3 -m venv .venv
    $ source .venv/bin/activate - activate virtual machine Python

В строке состояния VSC, выбрать пункт интерпретатора: "+ Введите путь к интерпретатору" -> "Найти:" - для поиска в файловом менеджере. Искать в каталоге проекта `.venv/bin/python3`. И так для каждого проекта.

Терминал VSC, открытый в проекте работает некорректно, поэтому можно добавить алиас в `$HOME/.bashrc`:

    alias python3="/path_to_project/.venv/bin/python"   - for the project start
    alias python="/usr/bin/python3.10"                  - for global start

## PIP of Python.

    $ pip3 install <name_biblio>        - install a module of the Python
    $ pip3 uninstall <name_biblio>      - deinstall a module
    $ pip3 list                         - list installed the modules
    $ pip3 freeze                       - list installed the modules
    $ pip3 freeze > requirements.txt    - create file with list installed modules, example, venv
    $ pip3 install -r requirements.txt  - install neadly modules in new project, example, venv

> С помощью команд `pip3 freeze > requirements.txt` и 
> `pip3 install -r > requirements.txt` удобно передавать/переносить проект 
> с одной машины на другую, или между разработчиками. 

> Копирование каталога `.venv` не позволит запустить проект в др. вирт окружении Python.
> Для передачи достаточно сами модули `*.py` и `requirements.txt`.

## GUI in Python.

FW:
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
4. [Download a video from YouTube with Pytube](https://pytube.io/en/latest/user/quickstart.html)
5. [Как проверить существование файла?](https://ru.stackoverflow.com/questions/414593/%D0%9A%D0%B0%D0%BA-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D1%82%D1%8C-%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0)
6. [Вынести путь папки в переменную в Python](https://ru.stackoverflow.com/questions/490672/%d0%92%d1%8b%d0%bd%d0%b5%d1%81%d1%82%d0%b8-%d0%bf%d1%83%d1%82%d1%8c-%d0%bf%d0%b0%d0%bf%d0%ba%d0%b8-%d0%b2-%d0%bf%d0%b5%d1%80%d0%b5%d0%bc%d0%b5%d0%bd%d0%bd%d1%83%d1%8e-%d0%b2-python?noredirect=1&lq=1)
7. [Sqlite3 Как проверить существование записи?](https://ru.stackoverflow.com/questions/1427936/sqlite3-%d0%9a%d0%b0%d0%ba-%d0%bf%d1%80%d0%be%d0%b2%d0%b5%d1%80%d0%b8%d1%82%d1%8c-%d1%81%d1%83%d1%89%d0%b5%d1%81%d1%82%d0%b2%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5-%d0%b7%d0%b0%d0%bf%d0%b8%d1%81%d0%b8?rq=1)
8. [python-telegram-bot.doc](https://docs.python-telegram-bot.org/en/v20.0a4/)
9. [Matplotlib: Научная графика в Python](https://pythonworld.ru/novosti-mira-python/scientific-graphics-in-python.html)
10. [CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)

