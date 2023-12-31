# Функция sorted принимает на вход любую коллекцию по которой можно
# итерироваться и возвращает отсортированный список.
# 🔥 Важно! Функция sorted может принимать не только списки, но и другие
# последовательности: строки, множества, кортежи, словари и т.п.. При этом
# функция всегда возвращает список.

my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')

# Метод sort осуществляет сортировку элементов списка без создания копии, inplace.

my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

# Функция принимает на вход последовательность, которая поддерживает порядок
# элементов, возвращает функция объект итератор с обратным порядком элементов.

my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)
rev_list = list(reversed(my_list))
print(rev_list)

for item in reversed(my_list):
    print(item)

# Если нам нужно развёрнутая версия списка логичные и удобнее использовать
# встроенный метод reverse.
my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print(my_list)

#  Разворот списка с использованием квадратных скобок —
# частный случай срезов
my_list = [4, 8, 2, 9, 1, 7, 2]
new_list = my_list[::-1]
print(my_list, new_list, sep='\n')

