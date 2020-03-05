def swap(A, i, j):
    t = A[i]
    A[i] = A[j]
    A[j] = t


def intersect(i1, i2):
    A = i1[0]
    B = i1[1]
    C = i2[0]
    D = i2[1]
    assert A <= B, "interval is ({},{})".format(A, B)
    assert C <= D, "interval is ({},{})".format(C, D)
    if C >= A and C <= B:
        return C, (D if D <= B else B)
    elif D >= A and D <= B:
        return A, D
    elif C < A and D >= B:
        return A, B
    return None


def left(i): return i[0]


def right(i): return i[1]


def partition(A, p, r):
    x = A[p]
    i = p - 1
    k = p - 1
    j = p
    c = x
    while j <= r:
        cur_c = intersect(c, A[j])
        c = cur_c if cur_c is not None else c
        if cur_c is not None:
            k = k + 1
            swap(A, k, j)
        elif right(A[j]) < left(c):
            i = i + 1
            swap(A, i, j)
            k = k + 1
            swap(A, k, j)
        # elif left(A[j]) > right(x): no-op
        j = j + 1
    return (A, (i + 1, k))


# performs in O(n) if all intervals have common interval
def fuzzy_sort(A):
    fuzzy_sort_it(A, 0, len(A) - 1)
    return A


def fuzzy_sort_it(A, p, r):
    if p < r:
        pivot = partition(A, p, r)[1]
        fuzzy_sort_it(A, p, left(pivot) - 1)
        fuzzy_sort_it(A, right(pivot) + 1, r)


def partition_(A):
    return partition(A, 0, len(A) - 1)


print(intersect((0, 1), (0.75, 2)))
print(intersect((0, 1), (2, 3)))
print(intersect((0, 2), (2, 3)))

print(partition_([(0, 5), (-1, 1), (0, 1), (0.5, 4), (1.5, 3), (-1, 0.25)]))
print(partition_([(-11, -1), (10, 20), (1, 5)]))
print(partition_([(1, 1), (-1, -1), (5, 5), (0, 0)]))

print(fuzzy_sort([(0, 5), (-1, 1), (0, 1), (0.5, 4), (1.5, 3), (-1, 0.25)]))
print(fuzzy_sort([(-11, -1), (10, 20), (1, 5)]))
print(fuzzy_sort([(1, 1), (-1, -1), (5, 5), (0, 0)]))
print(fuzzy_sort([(10, 11), (0, 5), (0, 3), (-5, -5), (0, 0), (32, 33)]))
print(fuzzy_sort([(0, 10), (0, 1), (1, 2), (2, 4), (5, 6)]))
print(fuzzy_sort([(3.5, 10), (3, 4), (0, 5), (2, 7)]))
