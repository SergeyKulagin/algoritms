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


def merge_nosentinel(a, start, middle, end):
    temp = a[start:end]
    i = start
    j = middle
    k = 0
    while i < middle and j < end:
        if a[i] < a[j]:
            temp[k] = a[i]
            i = i + 1
        else:
            temp[k] = a[j]
            j = j + 1
        k = k +1

    while i < middle:
        temp[k] = a[i]
        i = i + 1
        k = k + 1
    while j < end:
        temp[k] = a[j]
        j = j + 1
        k = k + 1

    for m in range(0, len(temp)):
        a[start + m] = temp[m]

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
    merge_nosentinel(a, start, middle, end)


l = [1, 3, 5, 7, 2, 4, 8, 10, 15]
print(mergesort(l))
print(mergesort([7,6,3,1]))
