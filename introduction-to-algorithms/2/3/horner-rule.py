def naive_polynomial_evaluation(a, x):
    res = 0
    for i in range(0, len(a)):
        res = res + a[i] * lvl(x, i)
    return res


def lvl(x, l):
    res = 1
    for i in range(1, l + 1):
        res = res * x
    return res

print(naive_polynomial_evaluation([1,2,3], 2))
