import sqlite3

db = sqlite3.connect('Users.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT
    )''')

db.commit()


def registration(user_login, user_password):
    if len(user_login) == 0:
        return

    if len(user_password) == 0:
        return

    cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
    if cursor.fetchone() is None:
        cursor.execute(
            f'INSERT INTO users VALUES ("{user_login}", "{user_password}")')
        db.commit()

        return 'Вы успешно зарегестрировались'

    else:
        return 'Такой аккаунт уже есть'

def login(user_login, user_password):
    if len(user_login) == 0:
        return

    if len(user_password) == 0:
        return

    cursor.execute(f'SELECT password FROM users WHERE login="{user_login}"')
    check_pass = cursor.fetchall()

    cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
    check_login = cursor.fetchall()

    if check_pass[0][0] == user_password and check_login[0][0] == user_login:
        print('Вы успешно вошли')
