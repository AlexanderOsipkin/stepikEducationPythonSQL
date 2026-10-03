import sqlite3

# Подключение к базе данных
db = sqlite3.connect("exchanger.db")
cur = db.cursor()
print("Успешно подключились к БД")

# Создание таблицы
cur.execute("""
CREATE TABLE IF NOT EXISTS users_balance (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Balance_RUB FLOAT NOT NULL,
    Balance_USD FLOAT NOT NULL,
    Balance_EUR FLOAT NOT NULL);""")

db.commit()
print("Таблица успешно создана")

# Добавление начального баланса при первом запуске
cur.execute("SELECT * FROM users_balance")
users = cur.fetchall()

if len(users) == 0:
    cur.execute("""
    INSERT INTO users_balance (Balance_RUB, Balance_USD, Balance_EUR)
    VALUES (?, ?, ?)
    """, (100000, 1000, 1000))

    db.commit()
    print("Начальный баланс успешно добавлен")

# Получение баланса пользователя
cur.execute("SELECT * FROM users_balance WHERE UserID = 1")
user = cur.fetchone()

if user is None:
    print("Ошибка: пользователь не найден.")
else:
    print("Добро пожаловать в наш обменный пункт!")
    print("Актуальный курс валют: 1 USD = 70 RUB, 1 EUR = 80 RUB, 1 USD = 0.87 EUR, 1 EUR = 1.15 USD")

    print("Ваш баланс:")
    print(f"RUB: {user[1]:.2f}")
    print(f"USD: {user[2]:.2f}")
    print(f"EUR: {user[3]:.2f}")

    print("Введите, какую валюту желаете получить (1 - RUB, 2 - USD, 3 - EUR):")

    currency_to = input("Ваш выбор: ")

    if currency_to not in ["1", "2", "3"]:
        print("Ошибка: выберите валюту цифрой 1, 2 или 3!")

    else:
        amount = input("Какую сумму желаете получить?")

        # Проверяем введенную сумму
        try:
            amount = float(amount.replace(",", "."))

            if amount <= 0:
                print("Ошибка: сумма должна быть больше нуля!")

            else:
                print("Какую валюту вы готовы предложить взамен(1 - RUB, 2 - USD, 3 - EUR)?")

                currency_from = input("Ваш выбор: ")

                if currency_from not in ["1", "2", "3"]:
                    print("Ошибка: выберите валюту цифрой 1, 2 или 3!")

                elif currency_from == currency_to:
                    print("Ошибка: нельзя обменивать валюту на ту же самую валюту!")

                else:
                    # Получаем баланс
                    balance_rub = user[1]
                    balance_usd = user[2]
                    balance_eur = user[3]

                    # Названия валют
                    currencies = {
                        "1": "RUB",
                        "2": "USD",
                        "3": "EUR"
                    }

                    # Расчёт необходимой суммы валюты для выдачи
                    if currency_to == "1" and currency_from == "2":
                        amount_from = amount / 70

                    elif currency_to == "1" and currency_from == "3":
                        amount_from = amount / 80

                    elif currency_to == "2" and currency_from == "1":
                        amount_from = amount * 70

                    elif currency_to == "2" and currency_from == "3":
                        amount_from = amount * 1.15

                    elif currency_to == "3" and currency_from == "1":
                        amount_from = amount * 80

                    elif currency_to == "3" and currency_from == "2":
                        amount_from = amount / 0.87

                    # Проверка доступности средств
                    if currency_from == "1":
                        balance_from = balance_rub
                    elif currency_from == "2":
                        balance_from = balance_usd
                    else:
                        balance_from = balance_eur

                    if amount_from > balance_from:
                        print(f"Ошибка: недостаточно {currencies[currency_from]}для обмена!")
                        print(f"Необходимо: {amount_from:.2f}")
                        print(f"Доступно: {balance_from:.2f}")

                    else:
                        # Изменение баланса
                        if currency_from == "1":
                            balance_rub -= amount_from
                        elif currency_from == "2":
                            balance_usd -= amount_from
                        else:
                            balance_eur -= amount_from

                        if currency_to == "1":
                            balance_rub += amount
                        elif currency_to == "2":
                            balance_usd += amount
                        else:
                            balance_eur += amount

                        # Сохранение изменений в бд
                        cur.execute("""
                        UPDATE users_balance
                        SET Balance_RUB = ?,
                            Balance_USD = ?,
                            Balance_EUR = ?
                        WHERE UserID = 1
                        """, (balance_rub, balance_usd, balance_eur))

                        db.commit()
                        print("Изменения в БД внесены и сохранены успешно")

                        print("Обмен успешно выполнен!")
                        print(f"Вы получили: {amount:.2f} {currencies[currency_to]}")
                        print(f"Вы отдали: {amount_from:.2f} {currencies[currency_from]}")

                        print("Ваш новый баланс:")
                        print(f"RUB: {balance_rub:.2f}")
                        print(f"USD: {balance_usd:.2f}")
                        print(f"EUR: {balance_eur:.2f}")

        except ValueError:
            print("Ошибка: введите корректную числовую сумму!")

# Закрытие соединения с бд
db.close()
print("БД успешно закрыта")
