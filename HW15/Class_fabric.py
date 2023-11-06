# Напишите код, который запускается из командной строки и
# получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл,
# флаг каталога,
# название родительского каталога.

import pathlib
from collections import namedtuple
import argparse
import logging

FORMAT = '{levelname}, {asctime}, {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='HW15/log_fab.log',
                    filemode='a', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)

DIRSUBJECT = namedtuple('DIRSUBJECT',
                        ['file_name', 'ext', 'flag', 'parent'])


def log_dec(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            logger.error(f'Ошибка {e} в функции {func.__name__}'
                         f' при некорректно указанном пути {args}')
        return None
    return wrapper


@log_dec
def dir_info(path):
    path = pathlib.Path(path)
    new_list = []
    for file in path.iterdir():
        new_list.append(DIRSUBJECT(file.name, file.suffix,
                                   file.is_dir(), file.parent))
    return new_list


def par():
    parser = argparse.ArgumentParser(description='Path info')
    parser.add_argument('-p', '--path', type=str, help='Path')
    args = parser.parse_args()
    directory = dir_info(args.path)
    return f'{directory}'


if __name__ == "__main__":
    print(par())

# C:\Users\ksmos\PycharmProjects\pythonProject\HW15
