class IndexedPriorityQueue:
    def __init__(self, degree, maxSize):
        if maxSize <= 0:
            raise RuntimeError('maxSize <= 0')
        self.D = max(2, degree)
        self.N = max(self.D + 1, maxSize)
        self.im = [-1 for i in range(self.N)]
        self.pm = [-1 for i in range(self.N)]
        self.child = [i*self.D+1 for i in range(self.N)]
        self.parent = [(i-1)/self.D for i in range(self.N)]
        self.values = [None for i in range(self.N)]
        self.sz = 0
    def size(self):
        return self.sz
    def isEmpty(self):
        return self.sz == 0
    def contains(self, ki):
        self.keyInBoundsOrThrow(ki)
        return self.pm[ki] != -1
    def peekMinKeyIndex(self):
        self.isNotEmptyOrThrow()
        return self.im[0]
    def pollMinKeyIndex(self):
        minki = self.peekMinKeyIndex()
        self.delete(minki)
        return minki
    def peekMinValue(self):
        self.isNotEmptyOrThrow()
        return self.values[self.im[0]]
    def pollMinValue(self):
        minValue = self.peekMinValue()
        self.delete(self.peekMinKeyIndex())
        return minValue
    def insert(self, ki, value):
        if self.contains(ki):
            raise RuntimeError(f'index already exists; received: {ki}')
        self.valueNotNullOrThrow(value)
        self.pm[ki] = self.sz
        self.im[self.sz] = ki
        self.values[ki] = value
        self.swim(self.sz)
        self.sz += 1
    def valueOf(self, ki):
        self.keyExistsOrThrow(ki)
        return self.values[ki]
    def delete(self, ki):
        self.keyExistsOrThrow(ki)
        i = self.pm[ki]
        self.sz -= 1
        self.swap(i, self.sz)
        self.sink(i)
        self.swim(i)
        value = self.values[ki]
        self.values[ki] = None
        self.pm[ki] = -1
        self.im[self.sz] = -1
        return value
    def update(self, ki, value):
        self.keyExistsAndValueNotNullOrThrow(ki, value)
        i = self.pm[ki]
        oldValue = self.values[ki]
        self.values[ki] = value
        self.sink(i)
        self.swim(i)
        return oldVAlue
    def decrease(self, ki, value):
        self.keyExistsAndValueNotNullOrThrow(ki, value)
        if value < self.values[ki]: #less
            self.values[ki] = value
            self.swim(self.pm[ki])
    def increase(self, ki, value):
        self.keyExistsAndValueNotNullOrThrow(ki, value)
        if self.values[ki] < value: #less
            self.values[ki] = value
            self.sink(self.pm[ki])
    def sink(self, i):
        j = self.minChild(i)
        while j!= -1:
            self.swap(i, j)
            i = j
            j = self.minChild(i)
    def swim(self, i):
        while i < self.parent[i]: #less
            self.swap(i, self.parent[i])
            i = parent[i]
    def minChild(self, i):
        index = -1
        _from = self.child[i]
        to = min(self.sz, _from + self.D)
        for j in range(_from,to):
            if j < i: #less
                index = i
                i = j
        return index
    def swap(self, i, j):
        self.pm[self.im[j]] = i
        self.pm[self.im[i]] = j
        tmp = self.im[i]
        self.im[i] = self.im[j]
        self.im[j] = tmp
    def __str__(self):
        return str(self.im)
    def isNotEmptyOrThrow(self):
        if self.isEmpty():
            raise RuntimeError('Priority queue underflow')
    def keyExistsAndValueNotNullOrThrow(self, ki, value):
        self.keyExistsOrThrow(ki)
        self.valueNotNullOrThrow(value)
    def keyExistsOrThrow(self, ki):
        if not self.contains(ki):
            raise RuntimeError(f'Index does not exist; received: {ki}')
    def valueNotNullOrThrow(self, value):
        if value is None:
            raise ValueError('Value cannot be null')
    def keyInBoundsOrThrow(self, ki):
        if ki < 0 or ki >= self.N:
            raise ValueError(f'Key index out of bounds; received: {ki}')


if __name__ == '__main__':
    heap = IndexedPriorityQueue(5, 10)
    heap.insert(3, 5)
    heap.decrease(3, 4)
    print(heap.valueOf(3))
    heap.insert(1, 1)
    heap.insert(5, 5)
    heap.increase(3, 2)
    heap.increase(3, 10)
    print(heap)
    heap.delete(1)
    print(heap)
    print(heap.peekMinValue())
