from rooting_a_tree import add_edge

def treeCenters(g: list[list[int]]):
    n = len(g)
    degree = [0] * n
    leaves = []
    for i in range(n):
        degree[i] = len(g[i])
        if degree[i] == 0 or degree[i] == 1:
            leaves.append(i)
            degree[i] = 0
    count = len(leaves)
    while count < n:
        new_leaves = []
        for node in leaves:
            for neighbor in g[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
            degree[node] = 0
        count += len(new_leaves)
        leaves = new_leaves
    return leaves

if __name__ == "__main__":
    graph = [[] for _ in range(9)]
    add_edge(graph, 0, 1)
    add_edge(graph, 2, 1)
    add_edge(graph, 2, 3)
    add_edge(graph, 3, 4)
    add_edge(graph, 5, 3)
    add_edge(graph, 2, 6)
    add_edge(graph, 6, 7)
    add_edge(graph, 6, 8)
    print(treeCenters(graph))
