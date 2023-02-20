import eel
# from DataBase import *
import json

eel.init('web')

@eel.expose
def send_data_to_json(data):

    # data = {
    #     'name': 'Абдул',
    #     'surname': 'Кумаров',
    #     'age': 15
    # }

    with open("data_file.json", "w", encoding='utf-8') as write_file:
        json.dump(data, write_file, indent=4)


eel.start('index.html', mode='chrome', size=(1200, 800))
