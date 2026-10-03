import os
import sqlite3
from dotenv import load_dotenv

"""Подключение к сущесвтующей БД"""
load_dotenv()
db_path = os.getenv("JOIN_PATH")

db = sqlite3.connect(db_path)
print("Подключились к базе даных")

cur = db.cursor()  # Переменная для управления базой даных

"""INNER JOIN"""

cur.execute("""SELECT PersonID, First_name, PositionID, Position
FROM Persons
INNER JOIN Positions ON PositionID = Position_ref;""")
result_all = cur.fetchall()
for result in result_all:
    print(result)
print("*" * 50)

"""LEFT JOIN"""

cur.execute("""SELECT PersonID, First_name, PositionID, Position
FROM Persons
LEFT JOIN Positions ON PositionID = Position_ref;""")
result_all = cur.fetchall()
for result in result_all:
    print(result)
print("*" * 50)

"""RIGHT JOIN"""
cur.execute("""SELECT PersonID, First_name, PositionID, Position
FROM Persons
RIGHT JOIN Positions ON PositionID = Position_ref;""")
result_all = cur.fetchall()
for result in result_all:
    print(result)
print("*" * 50)

"""FULL JOIN"""
cur.execute("""SELECT PersonID, First_name, PositionID, Position
FROM Persons
FULL JOIN Positions ON PositionID = Position_ref;""")
result_all = cur.fetchall()
for result in result_all:
    print(result)
print("*" * 50)