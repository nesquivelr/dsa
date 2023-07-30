def prefix_function(s: str):
    n = len(s)
    pi = [0]*n
    for i in range(1, n):
        j = pi[i-1]
        while j>0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

if __name__ == "__main__":
    print(prefix_function("abcabckfjdslafabcd"))

