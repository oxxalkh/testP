# Создайте функцию для сортировки файлов по директориям:
# видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые
# не подошли для сортировки.

import os
# import pathlib
#
#
# def sort_files(path):
#     os.chdir(path)
#     ext = {}
#     for i in path.iterdir():
#         if i.is_file():
#             ext[i.suffix] = ext.get(i.suffix, []) + [i]
#     for key, value in ext.items():
#         os.mkdir(key)
#         for file in value:
#             try:
#                  file.replace(path/key/file.name)
#             except PermissionError:
#                 continue
#
#
# sort_files(pathlib.Path(r"C:\Users\ksmos\PycharmProjects\pythonProject\Seminar07\test"))


def sort_files(path):
    """
    Сортирует файлы согласно их разрешений. Создает папку для каждого типа из них
    :param path:
    :return:
    """
    os.chdir(path)
    files = os.listdir()
    ext = {}
    for i in files:
        *_, extention = i.split(".")
        ext[extention] = ext.get(extention, []) + [i]
    for key, value in ext.items():
        os.mkdir(key)
        for i in value:
            os.replace(i, f"{key}\\{i}")


if __name__ == "__main__":
    sort_files(r"C:\Users\ksmos\PycharmProjects\pythonProject\Seminar07\test")


