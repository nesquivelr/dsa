from topological_sort import find_topological_ordering, Edge


def dag_shortest_path(graph, start):
    num_nodes = len(graph)
    top_sort = find_topological_ordering(graph)
    dist = [None]*num_nodes
    dist[start] = 0
    for i in range(num_nodes):
        node_index = top_sort[i]
        if dist[node_index] is not None:
            adjacent_edges = graph[node_index]
            if adjacent_edges is not None:
                for edge in adjacent_edges:
                    new_dist = dist[node_index] + edge.weight
                    if dist[edge.to] is None:
                        dist[edge.to] = new_dist
                    else:
                        dist[edge.to] = min(dist[edge.to], new_dist)
    return dist


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
    dists = dag_shortest_path(graph, 0)
    print(dists)
