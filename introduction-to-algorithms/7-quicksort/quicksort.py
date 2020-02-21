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

def quickSortStep(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSortStep(A, p, q - 1)
        quickSortStep(A, q, r)

def quickSort(A):
    quickSortStep(A, 0, len(A) - 1)
    return A

#Hoare partition
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


print(quickSort([2, 7, 10, 11, 3, 0]))
print(quickSort([14, 24, 46, 49, 96, 11, 17, 99, 3, 33, 41, 6, 51, 30, 31]))

print(quickSortHoare([2, 7, 10, 11, 3, 0]))
print(quickSortHoare([14, 24, 46, 49, 96, 11, 17, 99, 3, 33, 41, 6, 51, 30, 31]))
