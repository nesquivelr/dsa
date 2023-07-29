class Edge:
    def __init__(self, from_: int, to: int, weight: int):
        self.from_ = from_
        self.to = to
        self.weight = weight

def find_topological_ordering(g: dict[str, list[Edge]]):
    n = len(g)
    in_degree = [0] * n
    for i in range(n):
        for edge in g[i]:
            in_degree[edge.to] = in_degree[edge.to]+1

    q = []
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)
    
    print(q)
    index = 0
    order = [0]*n
    while q:
        at = q.pop()
        order[index] = at
        index += 1
        for edge in g[at]:
            in_degree[edge.to] = in_degree[edge.to] - 1
            if in_degree[edge.to] == 0:
                q.append(edge.to)
    if index != n:
        return None
    return order


if __name__ == "__main__":
    n = 7
    graph = {i: [] for i in range(n)}
    graph[0].append(Edge(0, 1, 3))
    graph[0].append(Edge(0, 2, 2))
    graph[0].append(Edge(0, 5, 3))
    graph[1].append(Edge(1, 3, 1))
    graph[1].append(Edge(1, 2, 6))
    graph[2].append(Edge(2, 3, 1))
    graph[2].append(Edge(2, 4, 10))
    graph[3].append(Edge(3, 4, 5))
    graph[5].append(Edge(5, 4, 7))

    ordering = find_topological_ordering(graph)
    print(ordering)
