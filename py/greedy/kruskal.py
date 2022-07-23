import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from collections import defaultdict
from heapq import heapify, heappush, heappop
from union_find import UnionFind

class Graph:
    def __init__(self):
        self.nodes = defaultdict(set)
        self.edges_list = []
        heapify(self.edges_list)

    def add_edge(self, node_1, node_2, cost):
        heappush(self.edges_list, (cost, node_1, node_2))
        self.nodes[node_1].add((node_2, cost))
        self.nodes[node_2].add((node_1, cost))

    def __str__(self):
        return str(self.__dict__)

    def kruskal(self):
        V =  len(self.nodes.keys())
        path = []
        union_find = UnionFind(V)
        while self.edges_list:
            cost, head, tail = heappop(self.edges_list)
            head -= 1
            tail -= 1
            if union_find.find(head) != union_find.find(tail):
                path.append((head, tail))
                union_find.unify(head, tail)
        return path

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
    graph = Graph()
    for edge in edges:
        graph.add_edge(*edge)

    path = graph.kruskal()
    print(path)
