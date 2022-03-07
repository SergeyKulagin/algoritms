from random import *


# Lomuto partition
def partition(A, p, r):
    x = A[r]
    j = p
    i = p - 1
    while j < r:
        if A[j] < x:
            i = i + 1
            t = A[i]
            A[i] = A[j]
            A[j] = t
        j = j + 1

    t = A[i + 1]
    A[i + 1] = A[r]
    A[r] = t
    return i + 1


def random_partition(A, p, r):
    random_pivot = randint(p, r)
    t = A[r]
    A[r] = A[random_pivot]
    A[random_pivot] = t
    return partition(A, p, r)


def quickSortStep(A, p, r):
    if p < r:
        q = random_partition(A, p, r)
        quickSortStep(A, p, q - 1)
        quickSortStep(A, q, r)


def quickSort(A):
    quickSortStep(A, 0, len(A) - 1)
    return A


# Hoare partition
def hoare_partition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1

    while True:
        while True:
            j = j - 1
            if A[j] <= x:
                break
        while True:
            i = i + 1
            if A[i] >= x:
                break

        if i < j:
            t = A[i]
            A[i] = A[j]
            A[j] = t
        else:
            return j


def quickSortStepHoare(A, p, r):
    if p < r:
        q = hoare_partition(A, p, r)
        quickSortStep(A, p, q)
        quickSortStep(A, q, r)


def quickSortHoare(A):
    quickSortStepHoare(A, 0, len(A) - 1)
    return A


# todo double check and test carefully
# multi partition
def multiPartition(A, p, r):
    x = A[p]
    i = p - 1
    j = p + 1
    k = p
    while j < r + 1:
        if A[j] < x:
            i = i + 1
            A[i] = A[j]
            k = k + 1
            A[j] = A[k]
            A[k] = x
        elif A[j] == x:
            k = k + 1
            A[j] = A[k]
            A[k] = x
        j = j + 1
    return (i + 1, k)


def quickSortStepMultiPartition(A, p, r):
    if p < r:
        q = multiPartition(A, p, r)
        quickSortStepMultiPartition(A, p, q[0] - 1)
        quickSortStepMultiPartition(A, q[1] + 1, r)


def quickSortMultiPartition(A):
    quickSortStepMultiPartition(A, 0, len(A) - 1)
    return A


print(quickSort([0, 0, 0]))
print(quickSort([2, 7, 10, 11, 3, 0]))
print(quickSort([14, 24, 46, 49, 96, 11, 17, 99, 3, 33, 41, 6, 51, 30, 31]))

print(quickSortHoare([2, 7, 10, 11, 3, 0]))
print(quickSortHoare([14, 24, 46, 49, 96, 11, 17, 99, 3, 33, 41, 6, 51, 30, 31]))

print(quickSortMultiPartition([2, 7, 10, 11, 3, 0]))
print(quickSortMultiPartition([14, 24, 46, 49, 96, 11, 17, 99, 3, 33, 41, 6, 51, 30, 31]))

# l = [5, 7, 7, 10, 5, 5, 3, 2, 1, 5, 12, 0, 99, 2]
# l = [18,3,3,3,3,1,1,1,1,7,7,7,7,12,12,17,17,18,0,0]
# l = [2, 1, 0, 4, 5]
# print(multiPartition(l, 0, len(l) - 1))
