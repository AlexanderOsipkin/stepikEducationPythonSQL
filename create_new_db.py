import sqlite3

"""Создание новой ДБ"""
db = sqlite3.connect('test_sql.db')
print("Подключились к базе даных")

cur = db.cursor()  # Переменная для управления базой даных

"""Создание таблицы в БД"""
cur.execute("""CREATE TABLE Students(
    StudentsID INTEGER PRIMARY KEY,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL);
""")

db.commit()  # Сохранение результата запроса
print("Создание таблицы")

"""Заполняем таблицу"""
# когда 1 значение
data_students = ('Alex', 'Petrov')
cur.execute("""INSERT INTO Students(First_name, Last_name)
    VALUES(?, ?);""", data_students)

db.commit()
print("Данные успешно добавлены")

# Когда несколько значений
data_students = [('Alex', 'Petrov'), ('Olga', 'Olgina')]
cur.executemany("""INSERT INTO Students(First_name, Last_name)
    VALUES(?, ?);""", data_students)

db.commit()
print("Данные успешно добавлены")


"""Отправка нескольких запросов"""

cur.executescript("""CREATE TABLE Students1(
    StudentsID INTEGER PRIMARY KEY,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL);
    
    INSERT INTO Students1(First_name, Last_name)
    VALUES('Alex', 'Petrov');
""")
db.commit()  # Сохранение результата запроса
print("Создание таблицы")