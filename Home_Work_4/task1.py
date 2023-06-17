# Напишите функцию для транспонирования матрицы

import numpy


def print_matrix(matrix_a):
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[i])):
            print(matrix_a[i][j], end=' ')
        print()


def reverse_matrix(matrix_b):
    new_matrix = list(zip(*matrix_b[::]))
    return new_matrix


matrix = numpy.array([[2, 3, 4, 5], [6, 7, 8, 9], [1, 2, 3, 4]])

print(matrix)
print()
print(matrix.T)
print()

my_matrix = [[2, 3, 4, 5], [6, 7, 8, 9], [1, 2, 3, 4]]
print_matrix(my_matrix)
print()
print_matrix(reverse_matrix(my_matrix))
