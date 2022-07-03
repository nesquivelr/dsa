from typing import List


def merge(a: List[int], b: List[int]):
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


def mergesort(low: int, high: int):
    if low < high:
        mid = (low + high)/2
        A = merge_sort(low, mid)
        B = merge_sort(mid+1, high)
        merge(low, mid, high)
    return input_list

def two_way_mergesort(input_list: List[int]):
    current_pass = []
    if len(input_list)%2==1:
        last_value = input_list.pop()
    else:
        last_value = None

    for i in range(0, len(input_list), 2):
        first_value = input_list[i]
        second_value = input_list[i+1]
        if first_value >= second_value:
            new_list = [second_value, first_value]
        else:
            new_list = [first_value, second_value]
        current_pass.append(new_list)

    if last_value is not None:
        last_list = current_pass.pop()
        current_pass.append(merge(last_list, [last_value]))


    while len(current_pass) != 1:
        if len(current_pass)%2==1:
            last_list = current_pass.pop()
            before_last_list = current_pass.pop()
            current_pass.append(merge(last_list, before_last_list))
        #print(current_pass)
        temporal_pass = []
        for i in range(0, len(current_pass), 2):
            first_part = current_pass[i]
            second_part = current_pass[i+1]
            temporal_pass.append(merge(first_part, second_part))
        current_pass = temporal_pass
    return current_pass[0]



if __name__ == '__main__':
    a = [2, 8, 15, 18]
    b = [5, 9, 12, 17, 500]
    print(merge(a,b))
    c = [9, 10, 3, 7, 5, 6, 4, 1, 8, 2]
    print('input=',c)
    print('output=',two_way_mergesort(c))
    #input_list = [9, 3, 7, 5, 6, 4, 8, 2]
    #print(input_list)
    #print(mergesort(input_list))
