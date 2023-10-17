# Функция получает на вход словарь с названием компании в качестве ключа и
# списком с доходами и расходами (3-10 чисел) в качестве значения. Вычислите
# итоговую прибыль или убыток каждой компании. Если все компании прибыльные,
# верните истину, а если хотя бы одна убыточная - ложь.

def company(name_comp: dict[str, float | int]) -> bool:
    for key, value in name_comp.items():
        if sum(value) < 0:
            return False
    return True

def is_profit(companys: dict[str, int | float]) -> bool:
    return all(map(lambda x: sum(x) > 0, companys.values()))

dt = {
    "Рога": [42, 73, 12, 85, -15, 2],
    "Копыта": [45, 25, 100.4, 22, 1],
    "Хвосты": [500, 123, 52, 45, 93]}

print(company(dt))
print(is_profit(dt))
