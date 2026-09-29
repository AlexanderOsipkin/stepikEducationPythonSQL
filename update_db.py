import sqlite3

"""Изменение данных в таблице"""

db = sqlite3.connect('test_sql.db')
print("Подключились к базе даных")

cur = db.cursor()  # Переменная для управления базой даных

update_params = ('Sokolov', 1)
cur.execute("""UPDATE Students1 SET Last_name = ? WHERE StudentsID = ?;""", update_params)
db.commit()
print("Данные успешно обновлены")
