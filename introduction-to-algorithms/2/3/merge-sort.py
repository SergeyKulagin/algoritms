def merge(a, start, middle, end):
    temp = []
    i = start
    j = middle
    for k in range(start, end):
        if a[i] <= a[j]:
            temp.append(a[i])
            i = i + 1
        else:
            temp.append(a[j])
            j = j + 1
    # todo the last element?
    temp.reverse()
    for m in range(start, end):
        a[m] = temp.pop()
    return a


print(merge([1, 3, 5, 2, 4], 0, 3, 4))
