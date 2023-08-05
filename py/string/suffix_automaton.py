class State:
    def __init__(self):
        self.len = 0
        self.link = 0
        self.next = {}

MAXLEN = 100000
st = [State() for _ in range(MAXLEN*2)]
sz = 0
last = 0

def sa_init():
    global sz, st, last
    st[0].len = 0
    st[0].link = -1
    sz += 1
    last = 0

def sa_extend(c: str):
    global sz, st, last
    cur = sz
    sz += 1
    st[cur].len = st[last].len + 1
    p = last
    while p != -1 and not c in st[p].next:
        st[p].next[c] = cur
        p = st[p].link
    if p == -1:
        st[cur].link = 0
    else:
        q = st[p].next[c]
        if st[p].len + 1 == st[q].len:
            st[cur].link = q
        else:
            clone = sz
            sz += 1
            st[clone].len = st[p].len + 1
            st[clone].next = st[q].next
            st[clone].link = st[q].link
            while p != -1 and st[p].next[c] == q:
                st[p].next[c] = clone
                p = st[p].link
            st[q].link = st[cur].link = clone
    last = cur

if __name__ == "__main__":
    sa_init()
    for char in "abcbc":
        sa_extend(char)
    print(st[0].len, st[0].link, st[0].next)
    print(last, st[1].next)
