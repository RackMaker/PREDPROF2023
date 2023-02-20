import eel
from dataBase import *
import json

eel.init('web')

data = {}

@eel.expose
def send_data_to_json(login, password):

    print(registration(login, password))



@eel.expose
def enter_to_account(login, password):

    with open("data_file.json", encoding='utf-8') as read_file:
        data_dict = json.load(read_file)


    if login in data_dict:
        print('Пользователь есть в базе')
        if password == data_dict[login]['password']:
            print('Пароль верный')
        else:
            print('Неправильный пароль')
    else:
        print('Пользователя нет в базе. Вам нужно зарегестрироваться')

eel.start('index.html', mode="yandex", size=(760, 760))
