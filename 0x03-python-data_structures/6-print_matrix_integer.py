#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
            for elem in range(len(matrix[row])):
                if elem != len(matrix[row]) - 1:
                    space = ' '
                else:
                    space = ''
                print("{:d}".format(matrix[row][elem]), end=space)
            print()
