# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

original_list = [2, 3, 5, 4, 1, 2, 2, 5, 0, 5, 10, 10, 10]


def find_duplicates(lst):
    # return list(set([i for i in lst if lst.count(i) > 1])) # в строку
    res_set = set()  # развернуто
    for i in lst:
        count_i = lst.count(i)
        if count_i > 1:
            res_set.add(i)
    return list(res_set)


print(
    f'{type(find_duplicates(original_list))} '
    f'{find_duplicates(original_list)}')

