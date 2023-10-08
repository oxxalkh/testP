# Напишите функцию для транспонирования матрицы.
from typing import List


def trans_matrix_1(mat):
    transposed = [[row[i] for row in mat] for i in range(len(mat[0]))]
    return transposed


def trans_matrix_2(mat: list) -> list[list]:
    return list(map(list, zip(*mat)))


matrix = [[1, 2, 3], [4, 5, 6]]
new_matrix_1 = trans_matrix_1(matrix)
print(*matrix, sep='\n')
print(*new_matrix_1, sep='\n')
new_matrix_2 = trans_matrix_2(matrix)
print(*new_matrix_2, sep='\n')
