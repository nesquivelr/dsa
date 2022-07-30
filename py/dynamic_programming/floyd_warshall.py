import math

def all_pairs_shortest_path(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                new_value = matrix[i][k] + matrix[k][j]
                if matrix[i][j] > new_value:
                    matrix[i][j] = new_value

if __name__ == '__main__':
    matrix = [
        [0, 3, math.inf, 7],
        [8, 0, 2, math.inf],
        [5, math.inf, 0, 1],
        [2, math.inf, math.inf, 0],
    ]
    all_pairs_shortest_path(matrix)
    for row in matrix:
        print(row)
