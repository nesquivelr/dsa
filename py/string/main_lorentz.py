from z_function import z_function, get_z

repetitions = []

def convert_to_repetitions(shift: int, left: bool, cntr: int, l: int, k1: int, k2: int):
    global repetitions
    l1 = max(1, l-k2)
    while l1 <= min(l, k1):
        if left and l1 == l:
            break
        l2 = l - l1
        pos = shift + (cntr-l1 if left else cntr-l-l1+1)
        repetitions.append((pos, pos+2*l-1))
        l1 += 1

def find_repetitions(s: str, shift: int=0):
    n = len(s)
    if n == 1:
        return
    nu = n//2
    nv = n - nu
    u = s[0:nu]
    v = s[nu:]
    ru = u[::-1]
    rv = v[::-1]
    find_repetitions(u, shift)
    find_repetitions(v, shift+nu)

    z1 = z_function(ru)
    z2 = z_function(v + "#" + u)
    z3 = z_function(ru + "#" + rv)
    z4 = z_function(v)

    for cntr in range(n):
        if cntr < nu:
            l = nu - cntr
            k1 = get_z(z1, nu - cntr)
            k2 = get_z(z2, nv+1+cntr)
        else:
            l = cntr - nu + 1
            k1 = get_z(z3, nu+1+nv-1-(cntr-nu))
            k2 = get_z(z4, (cntr-nu)+1)
        if k1 + k2 >= l:
            convert_to_repetitions(shift, cntr<nu, cntr, l, k1, k2)


if __name__ == "__main__":
    s = "acababaee"
    find_repetitions(s)
    for start, end in repetitions:
        print(s[start:end+1])
