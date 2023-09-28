my_set = {1, 2, 3, 4, 2, 5, 6, 7}
print(my_set)
my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
print(my_f_set)
# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']}TypeError: unhashable type:'list'

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set)
my_set.add(7)
print(my_set)
# my_set.add(9, 10)  # TypeError: set.add() takes exactly one argument (2 given)
my_set.add((9, 10))
print(my_set)

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.remove(5)
print(my_set)
# my_set.remove(10) # KeyError: 10
# При передаче несуществующего объекта получим ошибку KeyError

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.discard(5)
print(my_set)
my_set.discard(10)
# В отличии от remove при попытке удалить несуществующий элемент discard не
# вызывает ошибку. При этом множество не изменяется.

# Для получения пересечения множеств, т.е. множества с элементами, которые есть и
# в левом и в правам множестве используют метод intersection

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
# Новая версия Python позволяет получить пересечение множеств в следующей
# записи c использованием символа &
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set & other_set
print(f'{my_set = }\n{other_set = }\n{new_set = }')

# Для объединения множеств используется метод union.
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.union(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
new_set_2 = my_set | other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

# Метод difference удаляет из левого множества элементы правого.
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
new_set_2 = my_set - other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

# Для проверки входит ли элемент в множество используют зарезервированное
# слово in.
my_set = {3, 4, 2, 5, 6, 1, 7}
print(42 in my_set)


my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
print(len(my_set))
print(my_set - {1, 2, 3})
print(my_set.union({2, 4, 6, 8}))
print(my_set & {2, 4, 6, 8})
# print(my_set.discard(10))




