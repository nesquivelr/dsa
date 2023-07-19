from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

@dataclass
class TreeNode:
    id_: int
    parent: TreeNode
    children: list[Optional[TreeNode]]

def rootTree(g: list[list[int]], rootId: int = 0):
    root = TreeNode(rootId, None, [])
    return buildTree(g, root, None)

def buildTree(g: list[list[int]], node: TreeNode, parent: TreeNode):
    for childId in g[node.id_]:
        if parent and childId == parent.id_:
            continue
        child = TreeNode(childId, node, [])
        node.children.append(child)
        buildTree(g, child, node)
    return node

def add_edge(g: list[list[int]], from_: int, to: int):
    g[from_].append(to)
    g[to].append(from_)

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
    root = rootTree(graph, 6)
    print([node.id_ for node in root.children])
    print([node.id_ for node in root.children[0].children])
    print([node.id_ for node in root.children[0].children[1].children])
