'''
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.

'''
import json

#
# def to_json(old_file, new_file):
#     with open(old_file, "r") as f:
#???         data = {i.split()[0].capitalize(): float(i.split()[1]) for i in f.read().split('\n')}
#     with open(new_file, "w") as new_file:
#         json.dump(data, new_file, indent=4)

import json


def to_json(file_path):
    data = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            name, number = line.strip().split()
            name = name.capitalize()
            data[name] = float(number)

    json_data = json.dumps(data, indent=4)

    with open('new_json_file.txt', 'w') as output_file:
        output_file.write(json_data)

    print("Новый файл 'new_json_file.txt' успешно создан с данными в формате JSON.")


to_json('../Seminar07/output3.txt')

