# Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
def numbs_index(num: list[int], start: int, stop: int):
    if start > stop:
        start, stop = stop, start
    if start < 0:
        start = 0
    if stop > len(num) or stop < 0:
        stop = len(num)
    return sum(num[start:stop])


numb = [2, 6, -6, 5, 1]
print(numbs_index(numb, -10, -70))
