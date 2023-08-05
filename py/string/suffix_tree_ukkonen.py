"""TODO"""
from collections import defaultdict


class Node:
    def __init__(self, left: int = 0, right: int = 0, parent: int =-1):
        self.left = left
        self.right = right
        self.parent = parent
        self.suffix_link = -1
        self.next = defaultdict(lambda:-1)

    def len(self):
        return self.right - self.left

class State:
    def __init__(self, vertex: int, position: int):
        self.vertex = vertex
        self.position = position

def go(tree: list[Node], string: str, state: State, left: int, right: int) -> State:
    while left < right:
        if state.position == tree[state.vertex].len():
            state = State(tree[state.vertex].next[string[left]], 0)
            if state.vertex == -1:
                return state
        else:
            if string[tree[state.vertex].left+state.position] != string[left]:
                return State(-1, -1)
            if right - left < tree[state.veretex].len() - state.position:
                return State(state.vertex, state.position+right-left)
            left += tree[state.vertex].len() - state.position
            state.position = tree[state.vertex].len()
    return state

def split(state: State) -> int:
    if state.position == tree[state.vertex].len():
        return state.vertex
    if state.position == 0:
        return tree[state.vertex].parent
    vertex = tree[state.vertex]
    id_ = size
    size += 1
    tree[id_] = Node(vertex.left, vertex.left+state.position, vertex.parent)
    tree[vertex.parent].next[string[vertex.left]] = id_
    tree[id_].next[string[vertex.left+state.position]] = state.vertex
    tree[state.vertex].parent = id_
    tree[state.vertex].left += state.position
    return id_

def get_link(v: int) -> int:
    if tree[vertex].link != -1:
        return tree[vertex].link
    if tree[vertex].parent == -1:
        return 0
    to = get_link(tree[vertex].parent)
    tree[vertex].link = split(go(tree, state(to, tree[to].len())), tree[vertex].left + (tree[vertex].parent == 0, tree[vertex].right))
    return tree[vertex].link

def tree_extend(tree: list[Node], string: str, pointer: State, pos: int):
    while True:
        npointer = go(tree, string, pointer, pos, pos+1)
        if npointer != -1:
            pointer = npointer
            return
        mid = split(pointer)
        leaf = size
        size += 1
        tree[leaf] = Node(position, n, mid)
        t[mid].next[string[pos]] = leaf
        pointer.v = get_link(mid)
        pointer.pos = tree[pointer.v].len()
        if not mid:
            break

def build_tree(string: str):
    n = len(string)
    size = 1
    tree = [Node() for _ in range(n)]
    pointer = State(0, 0)
    for i in range(n):
        tree_extend(tree, string, pointer, i)
    return tree

if __name__ == "__main__":
    tree = build_tree("aaba")
