# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

a = [2, 3, 5, 4, 1, 2, 2, 5, 0, 5, 10, 10, 10]
for i in a:
    if a.count(i) >= 2:
        a.remove(i)
        a.remove(i)
print(a)

for i in set(a):
    if a.count(i) == 2:
        a.remove(i)
        a.remove(i)
print(a)


# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.
new_a = []
for n, el in enumerate(a, start= 1):
    if el % 2 != 0:
        new_a.append(n)
print(new_a)

# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был
# один пробел между ним и номером строки
n = input()
a = sorted(n.split())
max_len = 0
for el in a:
    if len(el) > max_len:
        max_len = len(el)
for n, el in enumerate(a, start=1):
    print(f'{n} {el:>{max_len}}')

k = 'fdfd iyitk fsagzg 9tjf63'
d = sorted(k.split())
max_len = len(max(d, key=len))
print(max_len)

for k, el in enumerate(d, start=1):
    print(f'{k} {el:>{max_len}}')
