from random import *

def rand_array_sorted(size, p, r):
    i = 0
    res = []
    while i < size:
        number = randint(p, r)
        res = res + [number]
        i = i + 1

    return sorted(res)



print(rand_array_sorted(10, 1, 100))
print(rand_array_sorted(10, 1, 100))