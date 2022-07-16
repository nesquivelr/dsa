def construct_tree(array, segtree, low, high, pos):
    if low == high:
        segtree[pos] = array[low]
    else:
        mid = (low + high)//2
        construct_tree(array, segtree, low, mid, 2*pos)
        construct_tree(array, segtree, mid+1, high, 2*pos+1)
        segtree[pos] = segtree[2*pos] + segtree[2*pos+1]

def calculate_sum(segtree, low, high, sum_from, sum_to, pos):
    if sum_from>sum_to:
        return 0
    if low == sum_from and high == sum_to:
        return segtree[pos]
    mid = (low + high)//2
    return calculate_sum(segtree, low, mid, sum_from, min(sum_to, mid), pos*2) \
            + calculate_sum(segtree, mid+1, high, max(sum_from, mid+1), sum_to, pos*2+1)

def update_tree(segtree, low, high, update_pos, update_val, pos):
    if low == high:
        segtree[pos] = update_val
    else:
        mid = (low + high)//2
        if update_pos <= mid:
            update_tree(segtree, low, mid, update_pos, update_val, pos*2)
        else:
            update_tree(segtree, mid+1, high, update_pos, update_val, pos*2+1)
        tree[pos] = tree[pos*2] + tree[pos*2+1]

if  __name__ == '__main__':
    array = [0,1,2,3,4,5,6,7,8,9]
    N = len(array)
    tree = [0 for _ in range(4*N)]
    t = construct_tree(array, tree, 0, N-1, 1)
    print(tree)
    print(calculate_sum(tree, 0, N-1, 0, 2, 1))
    print(calculate_sum(tree, 0, N-1, 5, 8, 1))
    update_tree(tree, 0, N-1, 2, 3, 1)
    print(calculate_sum(tree, 0, N-1, 0, 2, 1))
