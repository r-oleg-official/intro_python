## Create new database, open existing database.

	import sqlite3 as sq
	
	with sq.connect('database.db') as db:
		cursor = db.cursor()
		query = """CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name TEXT
		cursor.execute(query)


`sq.connect` - устанавливает соединение с БД, если файла нет то создается.
`cursor` - создается объект класса "`cursor()`", который будет перемещаться по БД и выполнять 
SQL-запросы с помощью метода `execute()`, аргументом которого и будет запрос к БД.

`CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name TEXT` - создать табл-цу, если такой нет 
с именем `expenses` (расходы) с двумя полями `id` и `name`.

Для SQLite есть 4 типа данных:
- NULL
- INTEGER - целочисленное со знаком, сохраненное в 1, 2, 3, 4, 6 и 8 байтах в зависимости от 
величины значения
- REAL - с плавающей точкой 8 байт
- TEXT - текст строка в зависимости т кодировки БД (UTF-8, UTF-16BE, или UTF-16LE)
- BLOB - значение в виде блока данных, хранится так как он был введен.

	query1 = """ INSERT INTO expenses (id, name) VALUES(1, 'Коммуналка') """
	query2 = """ INSERT INTO expenses (name, id) VALUES('Бензин', 2) """
	query3 = """ INSERT INTO expenses VALUES(3, 'Интернет') """
	cursor.execute(query1)
	cursor.execute(query2)
	cursor.execute(query3)
	db.commit()
	
Для `query3` имена полей не указаны, значит они будут вставляться в том порядке, в котором
хранятся в ней поля. Этот метод менее предпочителен.

Так делать некрасиво:

	cursor.execute(query1)
	cursor.execute(query2)
	cursor.execute(query3)
	
`db.commit()` - указано в офиц документации как обязательная, но будет работать и без нее. 
Нужна для обновления БД перед её закрытием.


## Example SQL-requests.

records = cursor.execute('''SELECT directory.id, users.surname, users.name, phones.phone_number,
                                types_of_number.type_of_number
                                FROM directory, users, phones, types_of_number
                                WHERE directory.user_id = users.id AND directory.phone_id = phones.id AND
                                phones.type_id = types_of_number.id ''').fetchall()

SELECT
	phones.id pid,
	phones.phone_number phn,
	users.surname sn,
	users.name n
FROM
	phones,
	users
WHERE
	directory.phone_id = pid
	AND
	directory.user_id = users.id
	AND
	sn = 'Иванов'
	AND n = 'Иван' phn = '+79991112233'

INSERT INTO phones (phone_number, type_id) VALUES (+79991112233, 3)

## Sources.

1. [10.5.4 MySQLCursor.execute() Method](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)
2. [Шаг 8 - Выбор данных из нескольких таблиц](https://firststeps.ru/sql/r.php?8)
3. [Сложная выборка из нескольких таблиц SQLite](https://ru.stackoverflow.com/questions/452783/%d0%a1%d0%bb%d0%be%d0%b6%d0%bd%d0%b0%d1%8f-%d0%b2%d1%8b%d0%b1%d0%be%d1%80%d0%ba%d0%b0-%d0%b8%d0%b7-%d0%bd%d0%b5%d1%81%d0%ba%d0%be%d0%bb%d1%8c%d0%ba%d0%b8%d1%85-%d1%82%d0%b0%d0%b1%d0%bb%d0%b8%d1%86-sqlite?rq=1)
4. [Выборка из нескольких таблиц inner join](https://ru.stackoverflow.com/questions/851628/%D0%92%D1%8B%D0%B1%D0%BE%D1%80%D0%BA%D0%B0-%D0%B8%D0%B7-%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D1%85-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86-inner-join)
5. [База данных SQLite в Python. Выборка, связь таблиц #2 | Базовый курс. Программирование на Python](https://www.youtube.com/watch?v=gm0p517EG7o&list=PLAMm2eUmBSn0oIY4MyyzGZY9ebtbZSHw0&index=30)
6. [Изучение SQLite3 за 30 минут! Практика на основе языка Python](https://www.youtube.com/watch?v=bmQPy89IZNk)
7. [методы fetchall, fetchmany, fetchone, iterdump](https://proproprogs.ru/modules/metody-fetchall-fetchmany-fetchone-iterdump)


