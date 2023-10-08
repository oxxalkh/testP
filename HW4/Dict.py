# Напишите функцию принимающую на вход только ключевые параметры и возвращающую
# словарь, где ключ — значение переданного
# аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте
# его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) ->
# {True: "rev", "YES": 'acc', 4: "stroka
from typing import Dict, Any


def dict_kwargs(**kwargs) -> dict[str | Any, str]:
    res_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            value = str(value)
        res_dict[value] = key
    return res_dict


print(dict_kwargs(rev=True, acc="YES", stroka=4))
