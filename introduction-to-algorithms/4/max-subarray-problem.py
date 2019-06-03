import sys


def findMaxSubArray(a):
    return findMaxSubArrayRecStep(a, 0, len(a))


def findMaxSubArrayRecStep(a, start, end):
    if start >= end - 1:
        return SubArrayInfo(float('-inf'), float('-inf'), float('-inf'))
    middle = round((start + end) / 2)
    leftMaxSubArrayInfo = findMaxSubArrayRecStep(a, start, middle)
    rightMaxSubArrayInfo = findMaxSubArrayRecStep(a, middle, end)
    middleMaxSubArrayInfo = findMaxSubArrayFromPoint(a, middle)
    maxSubArrayInfo = max(max(leftMaxSubArrayInfo, rightMaxSubArrayInfo), middleMaxSubArrayInfo)
    return maxSubArrayInfo


def max(subArrayInfoFirst, subArrayInfoSecond):
    if subArrayInfoFirst.sum > subArrayInfoSecond.sum:
        return subArrayInfoFirst
    else:
        return subArrayInfoSecond


def findMaxSubArrayFromPoint(a, point):
    leftSubArray = findMaxSubArrayFromPointDirected(a, point, -1)
    rightSubArray = findMaxSubArrayFromPointDirected(a, point, 1)
    return SubArrayInfo(leftSubArray.start, rightSubArray.end, leftSubArray.sum + rightSubArray.sum)


def findMaxSubArrayFromPointDirected(a, point, directionIndex):
    sum = 0
    maxSubArrayInfo = SubArrayInfo(float('-inf'), float('-inf'), float('-inf'))
    for k in range(point, 0, directionIndex):
        sum = sum + a[k]
        if sum > maxSubArrayInfo.sum:
            maxSubArrayInfo.sum = sum
            maxSubArrayInfo.start = k

    return maxSubArrayInfo


class SubArrayInfo:
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum
    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "], sum = " + str(self.sum)


print(findMaxSubArray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4]))