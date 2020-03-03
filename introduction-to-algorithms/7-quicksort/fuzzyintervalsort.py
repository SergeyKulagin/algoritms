def swap(A, i, j):
    t = A[i]
    A[i] = A[j]
    A[j] = t


def intersect(i1, i2):
    A = i1[0]
    B = i1[1]
    C = i2[0]
    D = i2[1]
    if C >= A and C <= B:
        return C, (D if D <= B else B)
    elif D >= A and D <= B:
        return A, D
    return None


def left(i): return i[0]
def right(i): return i[1]


# todo double check
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


print(intersect((0, 1), (0.75, 2)))
print(intersect((0, 1), (2, 3)))
print(intersect((0, 2), (2, 3)))

l = [(0, 5), (-1, 1), (0, 1), (0.5, 4), (1.5, 3), (-1, 0.25)]
print(partition(l, 0, 5))
