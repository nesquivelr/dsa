from tree_centers import treeCenters
from rooting_a_tree import add_edge, rootTree

def encode(node):
    if node is None:
        return ""
    labels = []
    for child in node.children:
        labels.append(encode(child))
    labels.sort()
    result = ""
    for label in labels:
        result += label
    return "(" + result + ")"

def trees_are_isomorphic(tree1, tree2):
    tree1_centers = treeCenters(tree1)
    tree2_centers = treeCenters(tree2)
    tree1_rooted = rootTree(tree1, tree1_centers[0])
    tree1_encoded = encode(tree1_rooted)
    for center in tree2_centers:
        tree2_rooted = rootTree(tree2, center)
        tree2_encoded = encode(tree2_rooted)
        if tree1_encoded == tree2_encoded:
            return True
    return False

if __name__ == "__main__":
    tree1 = [[] for _ in range(5)]
    add_edge(tree1, 2, 0)
    add_edge(tree1, 3, 4)
    add_edge(tree1, 2, 1)
    add_edge(tree1, 2, 3)
    tree2 = [[] for _ in range(5)]
    add_edge(tree2, 1, 0)
    add_edge(tree2, 2, 4)
    add_edge(tree2, 1, 3)
    add_edge(tree2, 1, 2)
    print(trees_are_isomorphic(tree1, tree2))
    tree = [[] for _ in range(10)]
    add_edge(tree, 0, 2)
    add_edge(tree, 0, 1)
    add_edge(tree, 0, 3)
    add_edge(tree, 2, 6)
    add_edge(tree, 2, 7)
    add_edge(tree, 1, 4)
    add_edge(tree, 1, 5)
    add_edge(tree, 5, 9)
    add_edge(tree, 3, 8)
    root0 = rootTree(tree, 0)
    print(encode(root0) == "(((())())(()())(()))")
