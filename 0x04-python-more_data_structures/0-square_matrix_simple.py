#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    MatrixSquared= []
    for row in matrix:
        MatrixSquared.append([c**2 for c in row])
    return MatrixSquared
