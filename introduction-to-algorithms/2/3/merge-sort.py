import sys

def merge(a, start, middle, end):
    temp = []
    i = 0
    j = 0
    left = a[start:middle]
    left.append(sys.maxsize)
    right = a[middle:end]
    right.append(sys.maxsize)
    for k in range(start, end):
        if left[i] <= right[j]:
            temp.append(left[i])
            i = i + 1
        else:
            temp.append(right[j])
            j = j + 1
    temp.reverse()
    for m in range(start, end):
        a[m] = temp.pop()
    return a


l = [1, 3, 5, 2, 4]
print(merge(l, 0, 3, 5))
print(l[1:3])
