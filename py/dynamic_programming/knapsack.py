def solve(P, WT, m, n, K):
    for i in range(n+1):
        for w in range(m+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif WT[i] <= w:
                K[i][w] = max(P[i]+K[i-1][w-WT[i]],K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    print(K[n][w])

if __name__ == '__main__':
     P = [0, 1, 2, 5, 6]
     WT = [0, 2, 3, 4, 5]
     m = 8
     n = 4
     K = [[0]*(m+1) for _ in range(n+1)]
     solve(P, WT, m, n, K)
