import math

class SparseTable:
    def __init__(self, values, op):
        self.n = len(values)
        self.P = int(math.log(self.n)/math.log(2))
        self.log2 = [0 for i in range(self.n+1)]
        self.dp = [[0 for i in range(self.n)] for j in range(self.P + 1)]
        self.it = [[0 for i in range(self.n)] for j in range(self.P + 1)]
        self.op = op

        for i in range(self.n):
            self.dp[0][i] = values[i]
            self.it[0][i] = i

        for i in range(2, self.n+1):
            self.log2[i] = self.log2[i//2] + 1

        for i in range(1, self.P+1):
            j = 0
            while j + (1<<i) <= self.n:
                leftInterval = self.dp[i-1][j]
                rightInterval = self.dp[i-1][j + (1<<(i-1))]
                if self.op == 'MIN':
                    self.dp[i][j] = min(leftInterval, rightInterval)
                    if leftInterval <= rightInterval:
                        self.it[i][j] = self.it[i-1][j]
                    else:
                        self.it[i][j] = self.it[i-1][j + (1<<(i-1))]
                elif self.op == 'MAX':
                    self.dp[i][j] = max(leftInterval, rightInterval)
                    if leftInterval >= rightInterval:
                        self.it[i][j] = self.it[i-1][j]
                    else:
                        self.it[i][j] = self.it[i-1][j + (1<<(i-1))]
                elif self.op == 'SUM':
                    self.dp[i][j] = leftInterval + rightInterval
                elif self.op == 'MULT':
                    self.dp[i][j] = leftInterval * rightInterval
                elif self.op == 'GCD':
                    self.dp[i][j] = math.gcd(leftInterval, rightInterval)
                j += 1
    def printTable(self):
        for row in self.dp:
            for value in row:
                print(f'{value:02d}, ', end='')
            print()
    def query(self, l, r):
        _len = r - l + 1
        p = self.log2[_len]
        if self.op == 'MIN':
            return min(self.dp[p][l], self.dp[p][r-(1<<p)+1])
        elif self.op == 'MAX':
            return max(self.dp[p][l], self.dp[p][r-(1<<p)+1])
        elif self.op == 'SUM':
            return self.sumQuery(l, r)
        elif self.op == 'MULT':
            return self.multQuery(l, r)
        elif self.op == 'GCD':
            return math.gcd(self.dp[p][l], self.dp[p][r-(1<<p)+1])
    def sumQuery(self, l, r):
        _sum = 0
        while l <= r:
            p = self.log2[r-l+1]
            _sum += self.dp[p][l]
            l += (1<<p)
        return _sum
    def multQuery(self, l, r):
        result = 1
        while l <= r:
            p = self.log2[r-l+1]
            result *= self.dp[p][l]
            l += (1<<p)
        return result

if __name__ == '__main__':
    values = [1, 2, -3, 2, 4, -1, 5]
    for operation in ['MIN', 'MAX', 'SUM', 'MULT', 'GCD']:
        sparse_table = SparseTable(values, operation)
        print(operation)
        print(sparse_table.query(1,4))
        sparse_table.printTable()
