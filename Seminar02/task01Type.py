# 1. Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

a = 10
b = 'eee'
c = 0.67
d = True
e = None
print(f' {type(a)} \n {type(b)} \n {type(c)} \n {type(d)} \n {type(e)}')

# 2.Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
data = [a, b, c, d, e]
for n, i in enumerate(data, start=1):
    if isinstance(i, int) or isinstance(i, str):
        print(n, i, id(i), hash(i), i.__sizeof__(), "true")
    else:
        print(n, i, id(i), hash(i), i.__sizeof__())



