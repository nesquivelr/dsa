def compute_hash(s: str):
    p = 31
    m = 1e9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value+(ord(c)-ord("a")+1)*p_pow)%m
        p_pow = (p_pow * p)%m
    return hash_value


if __name__ == "__main__":
    print(f"Polynomial Rolling Hash. p=31 m={1e9+9} ", compute_hash("abc"))
    print("SipHash", hash("abc"))
