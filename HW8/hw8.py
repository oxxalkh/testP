'''
написать программу, которая принимает на вход директорию и рекурсивно обходит
 эту директорию и все вложенные директории. Результаты обхода должны быть
 сохранены в нескольких форматах: JSON, CSV и Pickle.
Каждый результат должен содержать следующую информацию:

Путь к файлу или директории: Абсолютный путь к файлу или директории.
Тип объекта: Это файл или директория. Размер: Для файлов - размер в байтах, для
 директорий - размер, учитывая все вложенные файлы и директории в байтах. Важные детали:

Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.

Для файлов сохраните их размер в байтах.

Для директорий, помимо их размера, учтите размер всех файлов и директорий,
находящихся внутри данной директории, и вложенных директорий.

Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.

Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle.
Форматы файлов должны быть выбираемыми.

Для обхода файловой системы вы можете использовать модуль os.

Вам необходимо написать функцию traverse_directory(directory),
которая будет выполнять обход директории и возвращать результаты в виде списка словарей.
 После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle)
  с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
'''


import os
import json
import csv
import pickle

def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            result = {
                'Path': path,
                'Type': 'File',
                'Size': size
            }
            results.append(result)
        for name in dirs:
            path = os.path.join(root, name)
            size = get_directory_size(path)
            result = {
                'Path': path,
                'Type': 'Directory',
                'Size': size
            }
            results.append(result)
    return results

def get_directory_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            total_size += os.path.getsize(path)
        for dir in dirs:
            path_d = os.path.join(root, dir)
            total_size += get_directory_size(path_d)
    return total_size

def save_results_to_json(results, filename):
    with open(filename, 'w') as file:
        json.dump(results, file,  indent=4)

def save_results_to_csv(results, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)

def save_results_to_pickle(results, filename):
    with open(filename, 'wb') as file:
        pickle.dump(results, file)

# Пример использования
directory = r'C:\Users\ksmos\PycharmProjects\pythonProject\Lesson07File'
print(traverse_directory(directory))
results = traverse_directory(directory)

save_results_to_json(results, 'results.json')
save_results_to_csv(results, 'results.csv')
save_results_to_pickle(results, 'results.pickle')


# import os
# import json
# import csv
# import pickle
#
#
# def get_dir_size(start_path='.'):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(start_path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             total_size += os.path.getsize(fp)
#         for d in dirnames:
#             dp = os.path.join(dirpath, d)
#             total_size += get_dir_size(dp)
#     return total_size
#
#
# def save_results_to_json(results, file_name):
#     with open(file_name, 'w') as f:
#         json.dump(results, f)
#
#
# def save_results_to_csv(results, file_name):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Path', 'Type', 'Size'])
#         for result in results:
#             writer.writerow([result['Path'], result['Type'], result['Size']])
#
#
# def save_results_to_pickle(results, file_name):
#     with open(file_name, 'wb') as f:
#         pickle.dump(results, f)
#
#
# def traverse_directory(directory):
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for name in files:
#             path = os.path.join(root, name)
#             size = os.path.getsize(path)
#             results.append({'Path': path, 'Type': 'File', 'Size': size})
#         for name in dirs:
#             path = os.path.join(root, name)
#             size = get_dir_size(path)
#             results.append({'Path': path, 'Type': 'Directory', 'Size': size})
#     return results
