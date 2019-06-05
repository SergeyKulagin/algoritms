def squareMatrixMultiplyDirect(a, b):
    size = len(a)
    c = createEmptyMatrix(size)
    for i in range(0, size):
        for j in range(0, size):
            res = 0
            for k in range(0, size):
                res = res + a[i][k] * b[k][j]
            c[i][j] = res
    return c


def createEmptyMatrix(size):
    res = [None] * size
    for i in range(size):
        res[i] = [None] * size;
    return res


print(squareMatrixMultiplyDirect(
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
))
