def insertionSortAsc(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

# 2.1-2
def insertionSortDesc(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

# 2.3-4
def insertionSortRec(a):
    insertionSortRecIt(a, len(a) - 1)
    return a


def insertIntoSorted(a, idx):
    el = a[idx]
    insertIdx = idx
    for i in range(idx - 1, -1, -1):
        if el < a[i]:
            a[i + 1] = a[i]
            insertIdx = insertIdx - 1
    a[insertIdx] = el


def insertionSortRecIt(a, i):
    if i == 0:
        return
    insertionSortRecIt(a, i - 1)
    insertIntoSorted(a, i)

print(insertionSortAsc([2, 3, 1]))
print(insertionSortDesc([2, 3, 1]))
print(insertionSortRec([5,2,0,7,4,5]))
