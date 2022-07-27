def check_feasibility(matrix, row, column):
    print(matrix)
    size = len(matrix)
    for i in range(size):
        #print(f'[{row}][{i}] checked A')
        if matrix[row][i]:
            return False

    i = row-1
    j = column-1
    while i >= 0 and j >= 0:
        #print(f'[{i}][{j}] checked B')
        if matrix[i][j]:
            return False
        i -= 1
        j -= 1

    i = row+1
    j = column-1
    while i < size and j >= 0:
        #print(f'[{i}][{j}] checked C')
        if matrix[i][j]:
            return False
        i += 1
        j -= 1
    return True

def n_queens(matrix: list[list[int]], column: int):
    size = len(matrix)
    if column == size:
        return True
    for i in range(size):
        if check_feasibility(matrix, i, column):
            matrix[i][column] = 1
            if n_queens(matrix, column+1) is True:
                return True
            matrix[i][column] = 0
    return False


if __name__ == '__main__':
    size = 4
    matrix = [[0 for j in range(size)] for i in range(size)]

    n_queens(matrix, 0)
    for row in matrix:
        print(row)
