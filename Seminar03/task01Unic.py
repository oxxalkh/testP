# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.
lst = [2,5,8,9,2,'r','.',5,6,5,5,43,9]

res = []
for el in lst:
    if el not in res:
        res.append(el)
print(res)
print(list(set(lst)))