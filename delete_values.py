import sqlite3

"""Удаление данных в таблице"""

db = sqlite3.connect('test_sql.db')
print("Подключились к базе даных")

cur = db.cursor()  # Переменная для управления базой даных

delete_params = '5'
cur.execute("""DELETE FROM Students WHERE StudentsID = ?;""", delete_params)
db.commit()
print("Данные успешно удалены")
