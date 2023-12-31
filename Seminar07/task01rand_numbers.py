'''
Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. Первое число int,
второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000. Количество строк и имя файла передаются как аргументы функции.
'''
from random import randint, uniform


def rnd_num_pairs(count:int, file_name: str ):
    """
    Генерация рандомных чисел int и float в диапазоне от -1000 до 1000
    и их запись в файл в формате: int|float, одна пара значений - одна строка
    :param count:
    :param file_name:
    :return:
    """
    with open(file_name, "a", encoding="utf-8") as f:
        for i in range(count):
            f.write(f"{randint(-1000,1000)}|{uniform(-1000,1000)}\n")


if __name__ == "__main__":
    rnd_num_pairs(5, "random_numbers.txt")
