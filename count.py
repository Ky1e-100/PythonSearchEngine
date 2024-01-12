# Binary count from tutorial
def count(list, value):
    start = findstart(list, value)
    end = findend(list, value)
    if start == -1 or end == -1:
        return -1
    count = end - start + 1
    return count

def findstart(list, value):
    start = 0
    end = len(list) - 1

    while start <= end:
        midIndex = (start + end) // 2
        midVal = list[midIndex]

        if midIndex == 0 and list[0] == value:
            return midIndex

        if list[midIndex-1] < value and midVal == value:
            return midIndex
        
        elif value > midVal:
            start = midIndex + 1
        else: 
            end = midIndex - 1
    return -1

def findend(list, value):
    start = 0
    end = len(list) - 1

    while start <= end:
        midIndex = (start + end) // 2
        midVal = list[midIndex]

        if midIndex == (len(list) - 1) or list[midIndex+1] > value and midVal == value:
            return midIndex
        
        if value < midVal:
            end = midIndex - 1
        else:
            start = midIndex + 1
        
    return -1

# test = ["apple", "peach"]
# print(findstart(test, "peach"))
# print(count(test, "apple"))