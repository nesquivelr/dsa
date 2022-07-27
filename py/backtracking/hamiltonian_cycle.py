def create_adyacency_matrix(edges):
    max_edge = max(edges, key=lambda t:max(t[0], t[1]))
    max_node = max(max_edge[:2])+1
    matrix = [[0 for j in range(max_node)] for i in range(max_node)]
    for start, end in edges:
        matrix[start][end] = 1
        matrix[end][start] = 1
    return matrix

def hamiltonian(matrix: list[list[int]], solution: list[int], k: int):
    n = len(matrix)-1
    while True:
        next_vertex(matrix, solution, k)
        if solution[k] == 0:
            return
        if k == n:
            print(solution)
        else:
            hamiltonian(matrix, solution, k+1)

def next_vertex(matrix: list[list[int]], solution: list[int], k: int):
    n = len(matrix)-1
    while True:
        solution[k] = (solution[k]+1)%(n+1)
        if solution[k] == 0:
            return
        if matrix[solution[k-1]][solution[k]] != 0:
            j = 1
            while j <= k-1:
                if solution[j] == solution[k]:
                    break
                j += 1
            if j == k:
                if k<=n and matrix[solution[n-1]][solution[1]] != 0:
                    return
        

if __name__ == '__main__':
    edges = [
        (0, 1),
        (0, 4),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 0),
        (2, 3),
        (3, 4),
    ]
    matrix = create_adyacency_matrix(edges)

    max_edge = max(edges, key=lambda t:max(t[0], t[1]))
    max_node = max(max_edge[:2])+1
    solution = [0 for i in range(max_node)]
    hamiltonian(matrix, solution, 1)
