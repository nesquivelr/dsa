import math

def create_adjacency_matrix(edges: int, greater_node: int):
    matrix = [[0]*greater_node for _ in range(greater_node)]
    for i, j, cost in edges:
        matrix[i][j] = cost
    return matrix
    

def multistage_graph(
        n: int,
        matrix: list[list[int]],
        d: list[int],
        cost: list[int],
        path: list[int],
        stages: list[int]
    ):
    for i in range(n-1, 0, -1):
        min_ = math.inf
        for k in range(i+1, n+1):
            if matrix[i][k] and matrix[i][k] + cost[k] < min_:
                min_ = matrix[i][k] + cost[k]
                d[i] = k
        cost[i] = min_
    path[1] = 1
    path[stages] = n
    for i in range(2, stages):
        path[i] = d[path[i-1]]
    return path

if __name__ == '__main__':
    edges = [
        (1, 2, 2),
        (1, 3, 1),
        (1, 4, 3),
        (2, 5, 2),
        (2, 6, 4),
        (3, 5, 6),
        (3, 6, 7),
        (4, 6, 8),
        (4, 7, 9),
        (5, 8, 6),
        (6, 8, 4),
        (7, 8, 5),
    ]
    greater_edge = max(edges, key=lambda x: max(x[:2]))
    n = max(greater_edge[:2])
    matrix = create_adjacency_matrix(edges, n+1)
    cost = [0]*(n+1)
    d = [0]*(n+1)
    path = [0]*(4+1)
    multistage_graph(n, matrix, d, cost, path, 4)
    print(path[1:])
