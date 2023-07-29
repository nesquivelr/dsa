class TarjanSccSolverAdjacencyList:
    def __init__(self, graph: list[list[int]]):
        if graph is None:
            raise ValueError("Graph cannot be null")
        self.graph = graph
        self.n = len(self.graph)
        self.unvisited = -1
        self.ids = [self.unvisited]*n
        self.low = [0]*n
        self.sccs = [0]*n
        self.visited = [False]*n
        self.stack = []
        self.scc_count = 0
        self.id_ = 0


    def solve(self):
        for i in range(self.n):
            if self.ids[i] == self.unvisited:
                self.dfs(i)

    def dfs(self, at: int):
        self.ids[at] = self.low[at] = self.id_
        self.id_ += 1
        self.stack.append(at)
        self.visited[at] = True
        for to in self.graph[at]:
            if self.ids[to] == self.unvisited:
                self.dfs(to)
            if self.visited[to]:
                self.low[at] = min(self.low[at], self.low[to])
        if self.ids[at] == self.low[at]:
            while self.stack:
                node = self.stack.pop()
                self.visited[node] = False
                self.sccs[node] = self.scc_count
                if node == at:
                    break
            self.scc_count += 1


def add_edge(g: list[list[int]], from_: int, to: int):
    g[from_].append(to)

if __name__ == "__main__":
    n = 8
    graph = [[] for i in range(n)]
    add_edge(graph, 6, 0)
    add_edge(graph, 6, 2)
    add_edge(graph, 3, 4)
    add_edge(graph, 6, 4)
    add_edge(graph, 2, 0)
    add_edge(graph, 0, 1)
    add_edge(graph, 4, 5)
    add_edge(graph, 5, 6)
    add_edge(graph, 3, 7)
    add_edge(graph, 7, 5)
    add_edge(graph, 1, 2)
    add_edge(graph, 7, 3)
    add_edge(graph, 5, 0)

    solver = TarjanSccSolverAdjacencyList(graph)
    solver.solve()
    values = {}
    for i in range(n):
        if solver.sccs[i] not in values:
            values[solver.sccs[i]] = []
        values[solver.sccs[i]].append(i)

    print(solver.scc_count)

    for group, nodes in values.items():
        print(group, nodes)
