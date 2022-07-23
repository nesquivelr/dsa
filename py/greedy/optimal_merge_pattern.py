import operator

def merge_two_lists(a, b):
    output = []
    i = 0
    j = 0
    m = len(a)
    n = len(b)
    while i < m and j < n:
        if a[i] < b[j]:
            output.append(a[i])
            i += 1
        else:
            output.append(b[j])
            j += 1

    for k in range(i, m):
        output.append(a[k])

    for k in range(j, n):
        output.append(b[k])

    return output

def merge_pattern(lists: list[list[int]]):
    lens = [(len(list_), list_) for list_ in lists]
    while len(lens) > 1:
        min_tuple = min(lens, key=operator.itemgetter(0))
        lens.remove(min_tuple)
        len_1, list_1= min_tuple
        min2_tuple = min(lens, key=operator.itemgetter(0))
        lens.remove(min2_tuple)
        len_2, list_2= min2_tuple
        new_list = merge_two_lists(list_1, list_2)
        lens.append((len_1 + len_2, new_list))
    return lens[0][1]


if __name__ == "__main__":
    lists = [
        [i for i in range(20)],
        [i for i in range(30)],
        [i for i in range(10)],
        [i for i in range(5)],
        [i for i in range(30)],
    ]
    print(merge_pattern(lists))
