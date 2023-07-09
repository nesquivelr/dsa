import sys

def min_cost_recursive(keys: list[int], freq: list[int], low: int, high: int, level: int):
    if low > high:
        return 0
    min_value = sys.maxsize
    for i in range(low, high+1):
        val = (
            min_cost_recursive(keys, freq, low, i-1, level+1)+
            min_cost_recursive(keys, freq, i+1, high, level+1)+
            level * freq[i])
        if val < min_value:
            min_value = val
    return min_value

def min_cost_iterative(keys: list[int], freq: list[int]):
    n = len(keys)
    T = [[0]*n for _ in range(n)]
    for i in range(n):
        T[i][i] = freq[i]
    for l in range(2, n+1):
        for i in range(0, n-l+1):
            j = i + l - 1
            T[i][j] = sys.maxsize
            current_sum = sum(freq[i:j+1])
            for k in range(i, j+1):
                f1 = 0
                if k-1 >= i:
                    f1 = T[i][k-1]
                f2 = 0
                if k + 1 <= j:
                    f2 = T[k+1][j]
                val = current_sum + f1 + f2
                if val < T[i][j]:
                    T[i][j] = val
    return T[0][n-1]


def main():
    keys = [10, 20, 30, 40]
    frequencies = [4, 2, 6, 3]
    print(min_cost_recursive(keys, frequencies, 0, len(keys)-1, 1))
    print(min_cost_iterative(keys, frequencies))

if __name__ == "__main__":
    main()