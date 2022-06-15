class FenwickTree:
    def __init__(self, sz = None):
        if sz is None:
            raise RuntimeError('Error with the size of the tree')
        elif type(sz) is int:
            self.tree = [0 for i in range(sz + 1)]
        elif type(sz) is list:
            self.tree = sz
            for i in range(1, len(self.tree)):
                j = i + self.lsb(i)
                if j < len(self.tree):
                    self.tree[j] += self.tree[i]
    def lsb(self, i: int):
        return i & -i

    def prefixSum(self, i):
        _sum = 0
        while i != 0:
            _sum += self.tree[i]
            i &= ~self.lsb(i)
        return _sum

    def sum(self, i, j):
        if j < i:
            raise RuntimeError('Make sure j>=i')
        return self.prefixSum(j) - self.prefixSum(i-1)

    def add(self, i, k):
        while i < len(self.tree):
            self.tree[i] += k
            i += self.lsb(i)

    def set(self, i, k):
        value = self.sum(i, i)
        self.add(i, k - value)

    def __str__(self):
        return str(self.tree)


#doesn't work when we modify 0
if __name__ == '__main__':
    fwt = FenwickTree([i for i in range(50)])
    print([i for i in range(50)])
    print(fwt.sum(1, 1))
    fwt.add(1, 4)
    print(fwt.sum(1, 1))
    print(fwt.sum(1, 5))
