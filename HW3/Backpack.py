# # Создайте словарь со списком вещей для похода в качестве ключа и их массой
# # в качестве значения. Определите какие вещи
# # влезут в рюкзак передав его максимальную грузоподъёмность.
# # Достаточно вернуть один допустимый вариант.
# # *Верните все возможные варианты комплектации рюкзака.
import itertools


def possible_pack_backpack(itms, max_wght):
    combinations = []
    for i in range(1, len(itms) + 1):
        for sub in itertools.combinations(itms, i):
            total_wght = sum(itms[item] for item in sub)
            if total_wght <= max_wght:
                combinations.append(sub)
    return combinations


def pack_backpack(itms, max_wght):
    possible_items = []
    for item, weight in itms.items():
        if weight <= max_wght:
            possible_items.append(item)
            max_wght -= weight
    return possible_items


items = {
    'Палатка': 3,
    'Спальник': 2,
    'Коврик': 1,
    'Горелка': 0.5,
    'Посуда': 1.5,
    'Еда': 2,
    'Вода': 2.5
}

max_weight = int(input(f'Введите максимальный вес рюкзака '))

# Вариант 1: Вернуть один допустимый вариант
found_combination = pack_backpack(items, max_weight)
print("Один допустимый вариант:")
if found_combination:
    total_weight = sum(items[item] for item in found_combination)
    print(f"Вариант с общей массой {total_weight}:")
    for item in found_combination:

        print(f"- {item}: {items[item]}")
else:
    print("Нет допустимых вариантов")


# Вариант 2: Вернуть все возможные варианты комплектации рюкзака
possible_combinations = possible_pack_backpack(items, max_weight)
print("\nВсе возможные варианты комплектации рюкзака:")
if possible_combinations:
    for combination in possible_combinations:
        total_weight = sum(items[item] for item in combination)
        print(f"Вариант с общей массой {total_weight}:")
        for item in combination:
            print(f"- {item}: {items[item]}")
else:
    print("Нет допустимых вариантов")
