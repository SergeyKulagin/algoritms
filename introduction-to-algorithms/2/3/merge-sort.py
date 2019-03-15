def merge(a, start, middle, end):
    r = []
    j = middle
    for i in range(start, middle - 1):
        # todo
        if a[i] < a[j]:
            r.pop(a[i])
        else:
            r.pop(a[j])
            j = j + 1




