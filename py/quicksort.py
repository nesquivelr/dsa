def partition(A, low, high):
    pivot = A[low]
    i = low
    j = high
    while i<j:
        while A[i] <= pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i<j:
            A[i], A[j] = A[j], A[i]
    A[low], A[j] = A[j], A[low]
    return j

def quicksort(A, low, high):
    if low < high:
        j = partition(A, low, high)
        quicksort(A, 0, j)
        quicksort(A, j+1, high)
    return A


if __name__ == '__main__':
    input_list = [10, 16, 8, 12, 15, 6, 3, 9, 5]
    print(f'input={input_list}')
    print(f'output={quicksort(input_list, 0, len(input_list)-1)}')

