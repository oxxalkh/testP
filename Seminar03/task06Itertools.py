# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.



items = {
    'Lev': ('Палатка', 'Спальник','Коврик', 'Вода'),
    'Lena': ('Горелка', 'Посуда', 'Еда', 'Спальник'),
    'Lora': ('Аптечка', 'Спальник', 'Вода'),
}
res = set()
for i in items.values():
    if res == set():
        res = set(i)
    else:
        res = res & set(i)
print(res)

only_one = set()
for i in items.values():
    only_one = set(i)
    for j in items.values():
        if i == j:
            continue
        else:
            only_one -= set(j)
    print(only_one)

not_one = None
for name, i in items.items():
    for j in items.values():
        if i == j:
            continue
        elif not not_one and not_one != set():
            not_one = set(j)
        else:
            not_one &= set(j)
    print(name, not_one - set(i))
    not_one = None
