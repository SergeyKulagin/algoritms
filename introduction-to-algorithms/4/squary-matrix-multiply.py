def squareMatrixMultiplyRecursive(a, b):
    size = len(a)
    c = createEmptyMatrix(size)
    if size == 1:
        c[0][0] = a[0][0] * b[0][0]
        return c

    stepSize = int(size/2)

    #c11
    a11 = subMatrix(a, 0, 0, stepSize)
    a12 = subMatrix(a, 0, stepSize, stepSize)
    a21 = subMatrix(a, stepSize, 0, stepSize)
    a22 = subMatrix(a, stepSize, stepSize, stepSize)
    b11 = subMatrix(b, 0, 0, stepSize)
    b12 = subMatrix(b, 0, stepSize, stepSize)
    b21 = subMatrix(b, stepSize, 0, stepSize)
    b22 = subMatrix(b, stepSize, stepSize, stepSize)

    #c11
    c11 = matrixSum(
        squareMatrixMultiplyRecursive(a11, b11),
        squareMatrixMultiplyRecursive(a12, b21)
    )
    #c12
    c12 =  matrixSum(
        squareMatrixMultiplyRecursive(a11, b12),
        squareMatrixMultiplyRecursive(a12, b22)
    )
    #c21
    c21 = matrixSum(
        squareMatrixMultiplyRecursive(a21, b11),
        squareMatrixMultiplyRecursive(a22, b21)
    )
    #c22
    c22 = matrixSum(
        squareMatrixMultiplyRecursive(a21, b12),
        squareMatrixMultiplyRecursive(a22, b22)
    )
    return toMatrix(c11, c12, c21, c22)


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

def subMatrix(m, line, col, size):
    sub = createEmptyMatrix(size)
    for i in range(0, size):
        for j in range(0, size):
            sub[i][j] = m[i + line][j + col]
    return sub

def toMatrix(c11, c12, c21, c22):
    size = len(c11)
    c = createEmptyMatrix(len(c11) * 2)
    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = c11[i][j]

    for i in range(0, size):
        for j in range(0, size):
            c[i][j + size] = c12[i][j]

    for i in range(0, size):
        for j in range(0, size):
            c[i + size][j] = c21[i][j]

    for i in range(0, size):
        for j in range(0, size):
            c[i + size][j + size] = c22[i][j]
    return c


def matrixSum(c1, c2):
    size = len(c1)
    c = createEmptyMatrix(size)
    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = c1[i][j] + c2[i][j]

    return c

def createEmptyMatrix(size):
    res = [None] * size
    for i in range(size):
        res[i] = [None] * size
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

print(squareMatrixMultiplyRecursive(
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
))

print(squareMatrixMultiplyDirect(
    [
        [3, 5, 9, 7],
        [2, 8, 4, 4],
        [9, 2, 8, 4],
        [3, 5, 3, 7]
    ],
    [
        [7, 1, 2, 1],
        [0, 8, 0, 1],
        [1, 5, 7, 6],
        [5, 1, 2, 0]
    ]
))

print(squareMatrixMultiplyRecursive(
    [
        [3, 5, 9, 7],
        [2, 8, 4, 4],
        [9, 2, 8, 4],
        [3, 5, 3, 7]
    ],
    [
        [7, 1, 2, 1],
        [0, 8, 0, 1],
        [1, 5, 7, 6],
        [5, 1, 2, 0]
    ]
))
