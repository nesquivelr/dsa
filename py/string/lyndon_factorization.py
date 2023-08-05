def duval(s: str):
    n = len(s)
    i = 0
    factorization = []
    while i < n:
        j = i + 1
        k = i
        while j < n and s[k] <= s[j]:
            if s[k] < s[j]:
                k = i
            else:
                k += 1
            j += 1
        while i <= k:
            factorization.append(s[i:i+(j-k+1)])
            i += (j - k)
    return factorization

if __name__ == "__main__":
    print(duval("abab"))

