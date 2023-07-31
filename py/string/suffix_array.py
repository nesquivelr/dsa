def suffix_array(s: str):
    int_array = [ord(v) for v in s]
    alphabet = 256
    n = len(s)
    sa = [0]*n
    sa2 = [0]*n
    rank = [0]*n
    c = [0]*max(alphabet,n)
    for i in range(n):
        rank[i] = int_array[i]
        c[rank[i]] += 1
    for i in range(1, alphabet):
        c[i] += c[i-1]
    for i in range(n-1, -1, -1):
        c[int_array[i]] -= 1
        sa[c[int_array[i]]] = i
    p = 1
    while p < n:
        r = 0
        for i in range(n-p,n):
            sa2[r] = i
            r += 1
        for i in range(n):
            if sa[i] >= p:
                sa2[r] = sa[i] - p
                r += 1
        c = [0]*alphabet
        for i in range(n):
            c[rank[i]] += 1
        for i in range(1, alphabet):
            c[i] += c[i-1]
        for i in range(n-1,-1,-1):
            c[rank[sa2[i]]] -= 1
            sa[c[rank[sa2[i]]]] = sa2[i]
        sa2[sa[0]] = r = 0
        for i in range(1, n):
            if not(rank[sa[i-1]] == rank[sa[i]] and \
               sa[i-1]+p<n and \
               sa[i]+p<n and \
               rank[sa[i-1]+p] == rank[sa[i]+p]):
                r += 1
            sa2[sa[i]] = r
        rank, sa2 = sa2, rank
        if r == n-1:
            break
        p <<= 1
    return sa


if __name__ == "__main__":
    print(suffix_array("aaba"))
    print(suffix_array("banana$"))
