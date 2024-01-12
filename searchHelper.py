import sort

def binarySearch(list, target):
    start = 0
    end = len(list) -1
    mid = (start + end) // 2

    while start <= end:
        if target == list[mid]:
            return mid
        elif mid < target:
            start = mid + 1
        else:
            end = mid - 1 
    return -1

def binarySearchString(list, target):
        start = 0
        end = len(list) - 1
        while (start <= end): 
            mid = (start + end) // 2 
            if (list[mid] == target): 
                return mid
            elif (list[mid] < target): 
                start = mid + 1
            else: 
                end = mid - 1
        return -1  