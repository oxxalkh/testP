'''
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.

'''
import os
import pickle
import json
#
#
# def find_json(path):
#     for i in os.listdir(path):
#         if i.endswith(".json"):
#             *name, extention = i.split('.')
#             with open(i, 'r')as f:
#                 data = json.load(f)
#             with open('.'.join(name)+'.pickle', 'wb'):
#                 pickle.dump(data, f)
#
#
# find_json('../Seminar08')

def convert_json_to_pickle(directory):
    # Проверяем, существует ли указанная директория
    if not os.path.isdir(directory):
        print("Указанная директория не существует.")
        return

    # Получаем список файлов в директории
    files = os.listdir(directory)

    # Ищем json файлы и преобразуем их в pickle
    for file in files:
        if file.endswith(".json"):
            json_file_path = os.path.join(directory, file)
            print(json_file_path)
            pickle_file_path = os.path.join(directory, os.path.splitext(file)[0] + ".pickle")
            print(pickle_file_path)
            try:
                with open(json_file_path, "r") as json_file:
                    data = json.load(json_file)

                with open(pickle_file_path, "wb") as pickle_file:
                    pickle.dump(data, pickle_file)

                print(f"Файл {file} успешно преобразован в pickle.")
            except Exception as e:
                print(f"Ошибка при преобразовании файла {file}: {e}")

    print("Преобразование json файлов в pickle завершено.")

# Пример использования функции
convert_json_to_pickle("..\Seminar08")