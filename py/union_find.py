class UnionFind:
    def __init__(self, size : int = None):
        if size <= 0:
            print('Size <=0 is not allowed')
            raise
        else:
            self.size = size
            self.numComponents = size
            self.sz = [1 for i in range(size)]
            self.id = [i for i in range(size)]
    def find(self, p: int):
        root = p
        while root != self.id[root]:
            root = self.id[root]

        while p != root:
            _next = self.id[p]
            self.id[p] = root
            p = _next
        return root
    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)
    def componentSize(self, p: int):
        return sz[find(p)]
    def unify(self, p: int, q: int):
        root1 = self.find(p)
        root2 = self.find(q)
        if root1 == root2:
            return
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
        self.numComponents -= 1

if __name__ == '__main__':
    uf = UnionFind(10)
    print(uf.connected(2, 4))
    uf.unify(2, 1)
    uf.unify(3, 1)
    uf.unify(2, 4)
    print(uf.connected(2, 4))
