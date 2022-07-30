import math

def transform_matrix_dimensions(matrix_dimensions):
    dimensions = [value for tuple_ in matrix_dimensions for value in tuple_]
    d = []
    current_value = None
    for value in dimensions:
        if value != current_value:
            d.append(value)
            current_value = value
    return d

def matrix_chain_multiplication(dimensions):
    n = len(dimensions)
    matrix = [[0]*n for i in range(n)]
    order = [[0]*n for i in range(n)]
    for d in range(1, n-1):
        for i in range(1, n-d):
            j = i + d
            min_ = math.inf
            for k in range(i, j):
                current_value = (
                    matrix[i][k]
                    + matrix[k+1][j]
                    + dimensions[i-1]
                    * dimensions[k]
                    * dimensions[j]
                )
                if current_value < min_:
                    min_ = current_value
                    order[i][j] = k
            matrix[i][j] = min_
    return matrix, order

if __name__ == '__main__':
    matrix_dimensions = [
        (3, 2),
        (2, 4),
        (4, 2),
        (2, 5),
    ]
    dimensions = transform_matrix_dimensions(matrix_dimensions)
    matrix, order = matrix_chain_multiplication(dimensions)
    for row in matrix:
        print(row)
    print('*'*5)
    for row in order:
        print(row)
