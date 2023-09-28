
# list[start:stop:step]
# start указывает на первый индекс, который включается в срез. При отсутствии
# значения start равен нулю, началу списка.
# stop указывает на последний индекс, который не включается в срез. При отсутствии
# значения stop равен последнему элементу списка и включает его в срез.
# step — шаг движения от star до stop. По умолчанию step равен единице, все
# элементы по порядку.



my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:7:2])
print(my_list[:7:2])
print(my_list[2::2])
print(my_list[2:7:])
print(my_list[8:3:-1]) #reverse
print(my_list[3::])
print(my_list[:7:])



my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')


# матрица или список списков. для создания
# полной копии любой глубины вложенности используют функцию deepcopy из
# модуля copy.
import copy
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix)
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(len(my_list))
print(len(matrix))
print(len(matrix[1]))

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:6:2])
print(my_list.pop())
print(my_list.extend([314, 42]))
print(my_list)
print(my_list.sort(reverse=False))
print(my_list)


