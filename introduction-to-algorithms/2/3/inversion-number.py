import sys


def mergesort(a):
    return mergesortit(a, 0, len(a))


def mergesortit(a, start, end):
    if start >= end - 1:
        return 0
    middle = round((start + end) / 2)
    leftInversions = mergesortit(a, start, middle)
    rightInversions = mergesortit(a, middle, end)
    return merge(a, start, middle, end) + leftInversions + rightInversions


def merge(a, start, middle, end):
    inversions = 0
    lowerRights = 0
    i = 0
    j = 0
    left = a[start:middle]
    left.append(sys.maxsize)
    right = a[middle:end]
    right.append(sys.maxsize)
    for k in range(start, end):
        if left[i] <= right[j]:
            a[k] = left[i]
            i = i + 1
            inversions = inversions + lowerRights
        else:
            a[k] = right[j]
            j = j + 1
            # inversions = (inversions + lowerRights) + 1
            lowerRights = lowerRights + 1
    return inversions



print(mergesort([3,2,1,0,-1]))
