def z_function(s: str):
    n = len(s)
    z = [0]*n
    l = r = 0
    for i in range(1, n):
        if i<r:
            z[i] = min(r-i, z[i-1])
        while i+z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        if i+z[i] > r:
            l = i
            r = i + z[i]
    return z

def get_z(z: list[int], i: int):
    if 0 <= i < len(z):
        return z[i]
    else:
        return 0

if __name__ == "__main__":
    print(z_function("aaaaaa"))
