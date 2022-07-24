import math
from collections import defaultdict
from heapq import heappop, heappush

class Graph:
    def __init__(self):
        self.nodes = defaultdict(list)

    def add_edge(self, node_1, node_2, cost):
        self.nodes[node_1].append((node_2, cost))
        self.nodes[node_2]


    def dijkstra(self, start_node):
        heap = [(0, start_node)]
        visited = []
        path = {node: math.inf for node in self.nodes.keys()}
        path[start_node] = 0
        while heap:
            cost, node = heappop(heap)
            visited.append(node)
            for it_node, it_cost in self.nodes[node]:
                if it_node not in visited:
                    old_cost = path[it_node]
                    new_cost = path[node] + it_cost
                    if new_cost < old_cost:
                        heappush(heap, (new_cost, it_node))
                        path[it_node] = new_cost
        return path


if __name__ == '__main__':
    edges = [
        (0, 1, 2),
        (0, 2, 4),
        (1, 2, 1),
        (1, 3, 7),
        (2, 4, 3),
        (3, 5, 1),
        (4, 3, 2),
        (4, 5, 5),
    ]
    graph = Graph()
    for edge in edges:
        graph.add_edge(*edge)

    path = graph.dijkstra(0)
    print(path)
