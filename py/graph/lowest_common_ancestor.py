from rooting_a_tree import TreeNode, add_edge, rootTree

class Solver:
    def __init__(self):
        self.lca_node = None

    def lca(self, id1: int, id2: int):
        self.lca_node = None
        self.helper(root, id1, id2)
        return self.lca_node

    def helper(self, node: TreeNode, id1: int, id2: int):
        if node is None:
            return False
        count = 0
        if node.id_ == id1:
            count += 1
        if node.id_ == id2:
            count += 1
        for child in node.children:
            if self.helper(child, id1, id2):
                count += 1
        if count == 2:
            self.lca_node = node
        return count > 0

if __name__ == "__main__":
    n = 17
    tree = [[] for _ in range(n)]
    add_edge(tree, 0, 1)
    add_edge(tree, 0, 2)
    add_edge(tree, 1, 3)
    add_edge(tree, 1, 4)
    add_edge(tree, 2, 5)
    add_edge(tree, 2, 6)
    add_edge(tree, 2, 7)
    add_edge(tree, 3, 8)
    add_edge(tree, 3, 9)
    add_edge(tree, 5, 10)
    add_edge(tree, 5, 11)
    add_edge(tree, 7, 12)
    add_edge(tree, 7, 13)
    add_edge(tree, 11, 14)
    add_edge(tree, 11, 15)
    add_edge(tree, 11, 16)
    root = rootTree(tree, 0)
    solver = Solver()
    print(solver.lca(10, 15).id_)
