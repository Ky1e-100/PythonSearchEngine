#LECTURE CODE QUICK SORT

def quicksort(alist, low, high):
    if low < high:
        p = partition(alist, low, high)
        quicksort(alist, low, p)
        quicksort(alist, p+1, high)

def partition(alist, low, high):
    pivot = alist[low]
    i = low - 1
    j = high + 1

    while True:
        i = i + 1
        j = j - 1

        while alist[i] < pivot:
            i += 1
        while alist[j] > pivot:
            j -= 1
        if i >= j:
            return j

        temp = alist[i]
        alist[i] = alist[j]
        alist[j] = temp

# LECTURE MERGE SORT CODE
def merge(a, b):
    a_index = 0
    b_index = 0
    result = []

    while len(result) < len(a) + len(b):
        if a_index >= len(a): 
            result.append(b[b_index])
            b_index += 1
        elif b_index >= len(b): 
            result.append(a[a_index])
            a_index += 1
        elif a[a_index] < b[b_index]:
            result.append(a[a_index])
            a_index += 1
        else:
            result.append(b[b_index])
            b_index += 1

    return result

def merge_sort(alist):
    if len(alist) == 1:
        return alist

    left = merge_sort(alist[0:int(len(alist)/2)])
    right = merge_sort(alist[int(len(alist)/2):len(alist)])
    return merge(left, right)