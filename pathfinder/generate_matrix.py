import random
X = 10
Y = X

def generate_matrix(size):
    matrix = [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]
    matrix[0][0] = 1
    matrix[size-1][size-1] = 1

    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def has_path(matrix):
    pass

