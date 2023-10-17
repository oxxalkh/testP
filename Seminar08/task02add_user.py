"""
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.

"""

import json



def add_user():
    while True:
        name = input("Введите имя пользователя: ")
        id_us = input("Введите личный идентификатор пользователя: ")
        access_level = input("Введите уровень доступа пользователя (от 1 до 7): ")

        # Загрузка данных из файла, если файл уже существует
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        # Проверка на уникальность идентификатора пользователя
        unique_id = False
        while not unique_id:
            if id_us in data.values():
                print("Идентификатор уже занят. Пожалуйста, введите другой идентификатор.")
                id_us = input("Введите личный идентификатор пользователя: ")
            else:
                unique_id = True

        # Добавление новой информации в JSON файл
        if access_level not in data:
            data[access_level] = {}
        data[access_level][id_us] = name

        # Сохранение данных в файл
        with open("users1.json", "w") as file:
            json.dump(data, file)

        print("Пользователь успешно добавлен!")

add_user()

#
# def add_user2(name: str, id: str, level: str, file_name):
#     try:
#         with open("users2.json", "r") as f:
#             users = json.load(f)
#     except FileNotFoundError:
#         users = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}}
#     users[level][id] = name
#     with open(file_name, "w") as f:
#         json.dump(users, f)
#
#
# def request(file_name):
#     while True:
#         name = input("Введите имя пользователя: ")
#         id = input("Введите личный идентификатор пользователя: ")
#         level = input(
#             "Введите уровень доступа пользователя (от 1 до 7): ")
#         add_user2(name, id, level, file_name)
#
#
# # add_user('name1', '3', '5', 'users2.json')
# # add_user('name2', '8', '5', 'users2.json')
# # add_user('name3', '4', '7', 'users2.json')
# # add_user('name4', '1', '5', 'users2.json')
# request('users2.json')
