import os
import sqlite3
from dotenv import load_dotenv

"""Подключение к сущесвтующей БД"""
load_dotenv()
db_path = os.getenv("DB_PATH")

db = sqlite3.connect(db_path)
print("Подключились к базе даных")

cur = db.cursor()  # Переменная для управления базой даных

cur.execute("""SELECT * FROM Students;""")  # Запрос на получения полной таблицы Students
result_one = cur.fetchone()  # Одно значение
print(result_one[1])
result_many = cur.fetchmany(2)  # Несколько значений
print(result_many)
result_all = cur.fetchall()  # Все значения
print(result_all)
