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
result = cur.fetchall()  # результат запроса
print(result)
