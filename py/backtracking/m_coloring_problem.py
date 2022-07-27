from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = defaultdict(set)

    def add_edge(self, from_, to):
        self.nodes[from_].add(to)
        self.nodes[to].add(from_)

    def check_feasibility(self, solution: dict[int, str]):
        for node, neighbors in self.nodes.items():
            for neighbor in neighbors:
                if solution[node] == solution[neighbor]:
                    return False
        return True

    def color_graph(self, colors: list[str], solution: dict[int, str], start: int, current_nodes: int = 0):
        if current_nodes == len(self.nodes):
            return True
        for node in range(start, len(self.nodes)):
            for color in colors:
                previous_color = solution[node]
                solution[node] = color
                if self.check_feasibility(solution):
                    if self.color_graph(colors, solution, node+1, current_nodes+1) is True:
                        return True
                else:
                    continue
                solution[node] = previous_color
        return False

if __name__ == '__main__':
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
    ]
    colors = ['R', 'G', 'B']
    solution = [f'{i}' for i in range(len(edges))]

    graph = Graph()
    for edge in edges:
        graph.add_edge(*edge)

    graph.color_graph(colors, solution, 0, 0)
    print(solution)
