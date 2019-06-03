import sys


def findMaxSubArray(a):
    if len(a) == 0:
        return SubArrayInfo(None, None, None)
    return findMaxSubArrayRecStep(a, 0, len(a) - 1)


def findMaxSubArrayRecStep(a, start, end):
    if start >= end - 1:
        return SubArrayInfo(start, start, a[start])
    middle = round((start + end) / 2)
    leftMaxSubArrayInfo = findMaxSubArrayRecStep(a, start, middle)
    rightMaxSubArrayInfo = findMaxSubArrayRecStep(a, middle, end)
    middleMaxSubArrayInfo = findMaxSubArrayFromPoint(a, start, end, middle)
    maxSubArrayInfo = max(max(leftMaxSubArrayInfo, rightMaxSubArrayInfo), middleMaxSubArrayInfo)
    return maxSubArrayInfo


def max(subArrayInfoFirst, subArrayInfoSecond):
    if subArrayInfoFirst.sum > subArrayInfoSecond.sum:
        return subArrayInfoFirst
    else:
        return subArrayInfoSecond


def findMaxSubArrayFromPointLeft(a, point, to):
    sum = 0
    maxSubArrayInfo = SubArrayInfo(point, point, float('-inf'))
    for k in range(point, to, -1):
        sum = sum + a[k]
        if sum > maxSubArrayInfo.sum:
            maxSubArrayInfo.start = k
            maxSubArrayInfo.sum = sum
    return maxSubArrayInfo


def findMaxSubArrayFromPointRight(a, point, to):
    sum = 0
    maxSubArrayInfo = SubArrayInfo(point, point, float('-inf'))
    for k in range(point, to, 1):
        sum = sum + a[k]
        if sum > maxSubArrayInfo.sum:
            maxSubArrayInfo.end = k
            maxSubArrayInfo.sum = sum
    return maxSubArrayInfo


def findMaxSubArrayFromPoint(a, start, end, middle):
    leftSubArray = findMaxSubArrayFromPointLeft(a, middle, start)
    rightSubArray = findMaxSubArrayFromPointRight(a, middle + 1, end)
    return SubArrayInfo(leftSubArray.start, rightSubArray.end, leftSubArray.sum + rightSubArray.sum)


class SubArrayInfo:
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum

    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "], sum = " + str(self.sum)


print(findMaxSubArrayFromPointLeft(
    [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4],
    6,
    0
))

print(findMaxSubArrayFromPointRight(
    [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4],
    7,
    15
))

print(findMaxSubArrayFromPoint(
[13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4],
    0,
    15,
    6
))

print(findMaxSubArray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4]))
print(findMaxSubArray([]))
