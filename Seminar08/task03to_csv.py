'''
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.

'''
import csv
import json


def to_csv(file_json, file_csv):
    with open(file_json, "r", encoding='utf-8')as f:
        data = json.load(f)
    with open(file_csv,'w', encoding='utf-8')as f:
        write_csv = csv.DictWriter(f, fieldnames=['name', 'id', 'level'])
        for level, user in data.items():
            for id, name in user.items():
                write_csv.writerow({'name': name, 'id': id, 'level':level})



to_csv('users2.json', 'users2.csv')

