#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtrxSqr = []
    for row in matrix:
        mtrxSqr.append([c**2 for c in row])
    return mtrxSqr
