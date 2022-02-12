# todo double check, auto calculate digits number
def radixSort(a, digits_num):
    pos = 1
    while pos <= digits_num:
        fun = lambda e: int((e % (pos * 10)) / pos)
        sort(a, fun)
        pos = pos + 1
    return a


# use insertion sort that is stable
def sort(a, el_fun):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and el_fun(a[i]) > el_fun(key):
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a


print(radixSort([335, 777, 101, 202, 100], 2))
