import sqlite3

"""Удаление таблиц"""

db = sqlite3.connect('test_sql.db')
print("Подключились к базе даных")

cur = db.cursor()  # Переменная для управления базой даных

delete_params = '5'
cur.execute("""DROP TABLE Students_2""")
db.commit()
print("Таблица успешно удалена")
