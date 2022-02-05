def countSort(a, k):
    c = [0] * k
    for e in a:
        c[e] = c[e] + 1

    p = 0
    for idx, val in enumerate(c):
        c[idx] = c[idx] + p
        p = c[idx]

    print("helper array = " + str(c))

    l = len(a)
    b = [0] * l
    for idx, val in enumerate(a):
        end_idx = l - idx - 1
        c_idx = a[end_idx]
        b[c[c_idx] - 1] = c_idx
        c[c_idx] = c[c_idx] - 1

    print("result array = " + str(b))

    return b


countSort([1, 2, 3, 2, 2, 3, 7, 1], 10)
