import sys


def merge(a, start, middle, end):
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
        else:
            a[k] =right[j]
            j = j + 1
    return a


def mergesort(a):
    mergesortit(a, 0, len(a))
    return a


def mergesortit(a, start, end):
    if start >= end - 1:
        return
    middle = round((start + end) / 2)
    mergesortit(a, start, middle)
    mergesortit(a, middle, end)
    merge(a, start, middle, end)


l = [1, 3, 5, 7, 2, 4, 8, 10, 15]
print(mergesort(l))
print(mergesort([7,6,3,1]))
