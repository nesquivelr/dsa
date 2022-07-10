import itertools

def print_matrix(matrix):
    print('START_MATRIX')
    for row in matrix:
        print(row)
    print('END_MATRIX')

def split_matrix(matrix, slices):
    n_rows = len(matrix)
    start_1, end_1 = slices[0]
    start_2, end_2 = slices[1]
    size = n_rows//2
    new_matrix = [[None for _ in range(size)] for _ in range(size)]
    row_index = 0
    column_index = 0
    indexes = itertools.product(range(start_1, end_1), range(start_2, end_2))
    for index in indexes:
        index1, index2 = index
        #print(row_index, column_index)
        new_matrix[row_index][column_index] = matrix[index1][index2]
        if column_index < size-1:
            column_index += 1
        else:
            row_index += 1
            column_index = 0
    return new_matrix

def merge_matrices(A, B):
    size = len(A)
    C = []
    for i in range(size):
        C.append(A[i]+B[i])
    return C


def matrix_addition(A, B):
    size = len(A)
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrix_subtraction(A, B):
    size = len(A)
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = A[i][j] - B[i][j]
    return C

def mm(A, B):
    n = len(A)
    if n <= 2:
        C = [[0 for _ in range(n)] for _ in range(n)]
        C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
        C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
        C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
        C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]
        return C
    else:
        mid = n//2
        A00 = split_matrix(A,[[0, mid], [0, mid]])
        A01 = split_matrix(A,[[0, mid], [mid, n]])
        A10 = split_matrix(A,[[mid, n], [0, mid]])
        A11 = split_matrix(A,[[mid, n], [mid, n]])

        B00 = split_matrix(B,[[0, mid], [0, mid]])
        B01 = split_matrix(B,[[0, mid], [mid, n]])
        B10 = split_matrix(B,[[mid, n], [0, mid]])
        B11 = split_matrix(B,[[mid, n], [mid, n]])

        upper_left_add = matrix_addition(mm(A00,B00), mm(A01,B10))
        upper_right_add = matrix_addition(mm(A00,B01), mm(A01,B11))
        lower_left_add = matrix_addition(mm(A10,B00), mm(A11,B10))
        lower_right_add = matrix_addition(mm(A10,B01), mm(A11,B11))
        upper_part = merge_matrices(upper_left_add, upper_right_add)
        lower_part = merge_matrices(lower_left_add, lower_right_add)
        C = upper_part + lower_part
        return C

def mm_strassens(A, B):
    n = len(A)
    if n <= 2:
        C = [[0 for _ in range(n)] for _ in range(n)]
        C[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0]
        C[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1]
        C[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0]
        C[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1]
        return C
    else:
        mid = n//2
        A00 = split_matrix(A,[[0, mid], [0, mid]])
        A01 = split_matrix(A,[[0, mid], [mid, n]])
        A10 = split_matrix(A,[[mid, n], [0, mid]])
        A11 = split_matrix(A,[[mid, n], [mid, n]])

        B00 = split_matrix(B,[[0, mid], [0, mid]])
        B01 = split_matrix(B,[[0, mid], [mid, n]])
        B10 = split_matrix(B,[[mid, n], [0, mid]])
        B11 = split_matrix(B,[[mid, n], [mid, n]])

        P = mm_strassens(matrix_addition(A00,A11), matrix_addition(B00,B11))
        Q = mm_strassens(matrix_addition(A10,A11), B00)
        R = mm_strassens(A00, matrix_subtraction(B01, B11))
        S = mm_strassens(A11, matrix_subtraction(B10, B00))
        T = mm_strassens(matrix_addition(A00, A01), B11)
        U = mm_strassens(matrix_subtraction(A10,A00), matrix_addition(B00,B01))
        V = mm_strassens(matrix_subtraction(A01,A11), matrix_addition(B10,B11))

        upper_left_add = matrix_addition(matrix_subtraction(matrix_addition(P,S),T), V)
        upper_right_add = matrix_addition(R, T)
        lower_left_add = matrix_addition(Q, S)
        lower_right_add = matrix_addition(matrix_subtraction(matrix_addition(P, R), Q), U)

        upper_part = merge_matrices(upper_left_add, upper_right_add)
        lower_part = merge_matrices(lower_left_add, lower_right_add)
        C = upper_part + lower_part
        return C

def normal_multiplication(A, B):
    size = len(A)
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = 0
            for k in range(size):
                C[i][j] += A[i][k] * B[k][j]
    return C



if __name__ == '__main__':
    #This implementation is only for learning purposes and is not optimal
    #Better solutions should use numpy
    #Only works for squared matrices
    A = [
        [-2, 1],
        [0, 4],
    ]
    B = [
        [6, 5],
        [-7, 1]
    ]
    print_matrix(mm(A,B))
    print_matrix(normal_multiplication(A,B))
    A = [
        [5, 7, 9, 10],
        [2, 3, 3, 8],
        [8, 10, 2, 3],
        [3, 3, 4, 8],
    ]
    B = [
        [3, 10, 12, 18],
        [12, 1, 4, 9],
        [9, 10, 12, 2],
        [3, 12, 4, 10],
    ]
    print_matrix(mm(A,B))
    print_matrix(mm_strassens(A,B))
    A = [
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8]
    ]
    print_matrix(mm(A,A))
    print_matrix(mm_strassens(A,A))
