import sqlite3

# Подключение к бд
db = sqlite3.connect("registration.db")
cur = db.cursor()
print("Подключились к базе даных")

# Создаем таблицу
cur.execute("""CREATE TABLE IF NOT EXISTS users_data (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Login TEXT NOT NULL,
    Password TEXT NOT NULL,
    Code TEXT NOT NULL);
    """)

db.commit()
print("Таблица успешно создана")

# Добавление пользователя Иван
user_name = "Ivan"
user_pass = "qwer1234"
user_code = "1234"

cur.execute("""SELECT * FROM users_data""")
users = cur.fetchall()

ivan_exists = False

for user in users:
    if user[1].lower() == "ivan":
        ivan_exists = True

if ivan_exists == False:
    cur.execute("""
    INSERT INTO users_data (Login, Password, Code)
    VALUES (?, ?, ?);""", (user_name, user_pass, user_code))

    db.commit()
    print("Пользователь Иван успешно добавлен")

# Меню программы
print("Выберите действие:")
print("1 - Регистрация")
print("2 - Авторизация")
print("3 - Восстановление пароля")

action = input("Введите номер действия: ")

# 1. Регистрация
if action == "1":

    print("Регистрация нового пользователя")

    login = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    code = input("Введите 4-значный проверочный код: ")

    # Проверка обязательных полей
    if login == "" or password == "" or code == "":
        print("Ошибка: все поля обязательны для заполнения!")

    # Проверка кода
    elif len(code) != 4 or code.isdigit() == False:
        print("Ошибка: Проверочный код должен состоять из 4 цифр.")

    else:
        # Проверяем, существует ли такой Login
        cur.execute("SELECT * FROM users_data")
        users = cur.fetchall()

        login_exists = False

        for user in users:
            if user[1].lower() == login.lower():
                login_exists = True

        if login_exists:
            print("Ошибка: пользователь с таким именем уже существует!")

        else:
            cur.execute("""INSERT INTO users_data (Login, Password, Code)
            VALUES (?, ?, ?);""", (login, password, code))

            db.commit()
            print("Регистрация успешно завершена!")


# 2. Авторизация
elif action == "2":

    print("Авторизация пользователя")

    login = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    cur.execute("""SELECT * FROM users_data""")
    users = cur.fetchall()

    user_found = False

    for user in users:
        if user[1].lower() == login.lower():

            user_found = True

            if user[2] == password:
                print("Авторизация успешно выполнена!")
            else:
                print("Ошибка: неверный пароль!")

    if user_found == False:
        print("Ошибка: пользователь с таким именем не найден.")


# 3. Восстановление пароля
elif action == "3":

    print("Восстановление пароля")

    login = input("Введите имя пользователя: ")
    code = input("Введите проверочный код: ")
    new_password = input("Введите новый пароль: ")

    # Проверка обязательных полей
    if login == "" or code == "" or new_password == "":
        print("Ошибка: все поля обязательны для заполнения!")

    # Проверка кода
    elif len(code) != 4 or code.isdigit() == False:
        print("Ошибка: Проверочный код должен состоять из 4 цифр.")

    else:
        cur.execute("""SELECT * FROM users_data""")
        users = cur.fetchall()

        user_found = False

        for user in users:
            if user[1].lower() == login.lower():

                user_found = True

                if user[3] == code:

                    cur.execute("""UPDATE users_data 
                    SET Password = ?
                    WHERE UserID = ?
                    """, (new_password, user[0]))

                    db.commit()
                    print("Пароль успешно изменён!")

                else:
                    print("Ошибка: неверный проверочный код.")

        if user_found == False:
            print("Ошибка: пользователь с таким именем не найден.")


# Если введено что-то кроме 1, 2, 3
else:
    print("Ошибка: необходимо выбрать действие 1, 2 или 3")

# Закрытие соединения с бд
db.close()
print("База данных успешно закрыта")
