from random import *

alphabet = "abcdefghijklmnopqrstuvwxyz"

def rand_array_sorted(size, p, r):
    i = 0
    res = []
    while i < size:
        number = randint(p, r)
        res = res + [number]
        i = i + 1

    return sorted(res)


def rand_string(size):
    return ''.join(choice(alphabet) for i in range(size))


print(rand_string(20))