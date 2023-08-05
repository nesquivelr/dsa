class Vertex:
    def __init__(self, p: int =-1, char: str = "$"):
        alphabet_size = 26
        self.next = [-1]*alphabet_size
        self.output = False
        self.p = p
        self.pch = char
        self.link = -1
        self.go = [-1]*alphabet_size


def add_string(trie: list[Vertex], string: str):
    vertex = 0
    for char in string:
        char_ascii = ord(char) - ord("a")
        if trie[vertex].next[char_ascii] == -1:
            trie[vertex].next[char_ascii] = len(trie)
            trie.append(Vertex(vertex, char))
        vertex = trie[vertex].next[char_ascii]
    trie[vertex].output = True

def get_link(trie: list[Vertex], vertex: int) -> int:
    if trie[vertex].link == -1:
        if vertex == 0 or trie[vertex].p == 0:
            trie[vertex].link = 0
        else:
            trie[vertex].link = go(trie, get_link(trie, trie[vertex].p), trie[vertex].pch)
    return trie[vertex].link

def go(trie: list[Vertex], vertex: int, char: str) -> int:
    char_ascii = ord(char) - ord("a")
    if trie[vertex].go[char_ascii] == -1:
        if trie[vertex].next[char_ascii] != -1:
            trie[vertex].go[char_ascii] = trie[vertex].next[char_ascii]
        else:
            if vertex == 0:
                trie[vertex].go[char_ascii] = vertex
            else:
                trie[vertex].go[char_ascii] = go(trie, get_link(trie, vertex), char)
    return trie[vertex].go[char_ascii]

if __name__ == "__main__":
    trie = [Vertex()]
    strings = ["a", "ab", "bab", "bc", "bca", "c", "caa"]
    for string in strings:
        add_string(trie, string)
    print(len(trie))
    vertex = 0
    vertex = go(trie, vertex, "a")
    print(trie[vertex].output)
    vertex = go(trie, vertex, "b")
    print(trie[vertex].output)
    vertex = go(trie, vertex, "c")
    print(trie[vertex].output)
    vertex = go(trie, vertex, "d")
    print(trie[vertex].output)
    print(vertex)
