# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах
# отгадывания.
# � Для хранения используйте защищённый словарь уровня
# модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# � Для формирования результатов используйте генераторное
# выражение.

__all__ = ['mystery', 'mystery_dict', 'show_res']
_res_dict = {}


def mystery(myst: str, answ: list[str], count: int) -> int:
    for i in range(1, count + 1):
        answ_input = input('Введите отгадку ')
        if answ_input in answ:
            _archive(myst, i)
            return i
    _archive(myst, 0)
    return 0


def show_res():
    global _res_dict
    print(_res_dict)


def mystery_dict(count):
    mystery_box = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
                   'Не лает, не кусает, в дом не пускает': ['замок'],
                   'Сидит дед во сто шуб одет': ['лук', 'луковица'], }
    for key, value in mystery_box.items():
        print(key)
        print(mystery(key, value, count))


def _archive(mys: str, count: int):
    global _res_dict
    _res_dict[mys] = count


if __name__ == '__main__':
    # myst = 'Зимой и летом одним цветом.'
    # my_answ = ['ель', 'ёлка', 'сосна']
    count_a = 3
    # print(mystery(myst, my_answ, count_a))
    mystery_dict(count_a)
    show_res()
