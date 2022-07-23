import math


def create_adyacency_matrix(edges):
    max_edge = max(edges, key=lambda t:max(t[0], t[1]))
    max_node = max(max_edge[:2])
    matrix = [[0 for j in range(max_node)] for i in range(max_node)]
    for start, end, cost in edges:
        start -= 1
        end -= 1
        matrix[start][end] = cost
        matrix[end][start] = cost
    return matrix

def prim(matrix):
    V = len(matrix)
    visited = [False for i in range(V)]
    n_edges = 0
    visited[0] = True
    total_cost = 0

    head = 0
    tail= 0
    path = []
    while n_edges < V - 1:
        min_cost = math.inf
        for i in range(V):
            if visited[i]:
                for j in range(V):
                    if not visited[j] and matrix[i][j]:
                        if matrix[i][j] < min_cost:
                            total_cost += matrix[i][j]
                            min_cost = matrix[i][j]
                            head = i
                            tail = j
        visited[tail] = True
        path.append((head, tail))
        n_edges += 1
    return path, total_cost


        

if __name__ == '__main__':
    edges = [
        (1, 2, 28),
        (2, 7, 14),
        (2, 3, 16),
        (3, 4, 12),
        (4, 5, 22),
        (4, 7, 18),
        (5, 7, 24),
        (5, 6, 25),
        (6, 1, 10),
    ]
    matrix = create_adyacency_matrix(edges)
    path, total_cost = prim(matrix)
    print(path)
