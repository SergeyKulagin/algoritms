from random import *

from util import rand_array_sorted


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        res = self.findMedianSortedArrays_(self, nums1, nums2)
        median_el = res[0]
        return (median_el[0] + median_el[1]) / 2

    def findMedianSortedArrays_(self, nums1, nums2):
        assert len(nums1) + len(nums2) > 0, "Both arrays are empty"
        (small, big) = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        full_len = len(nums1) + len(nums2)
        middle_el = int(full_len / 2)
        median_index = (middle_el - 1, middle_el) if full_len % 2 == 0 else (middle_el, middle_el)
        one_point_median = median_index[0] == median_index[1]
        if len(small) == 0:
            return ((big[median_index[0]], big[median_index[1]]), median_index)

        p = 0
        r = len(small) - 1
        left_big_cursor = None
        while p <= r:
            m = int((p + r) / 2)
            res = self.binarySearch(self, big, 0, len(big) - 1, small[m])
            cur_idx = res[2] + m + 1
            if cur_idx <= median_index[1]:
                left_big_cursor = res[2]
                left_small_cursor = m
                p = m + 1
            else:
                r = m - 1

        # it means the small array is fully to the right from the median
        if left_big_cursor is None:
            if median_index[0] < len(big) - 1:
                median_el = (big[median_index[0]], big[median_index[1]])
            elif median_index[0] == len(big) - 1:
                median_el = (big[median_index[0]], big[median_index[1]] if one_point_median else small[0])
            else:
                median_el = (small[median_index[0] - len(big)], small[median_index[1] - len(big)])
        elif left_big_cursor + left_small_cursor + 1 == median_index[0]:
            median_el = (small[left_small_cursor],
                         small[left_small_cursor] if one_point_median else big[left_big_cursor + 1])
        elif left_big_cursor + left_small_cursor + 1 == median_index[1]:
            if one_point_median:
                median_el = (small[left_small_cursor], small[left_small_cursor])
            else:
                median_el = (self.biggest(self, big[left_big_cursor],
                                          big[left_big_cursor] if left_small_cursor == 0 else small[
                                              left_small_cursor - 1]), small[left_small_cursor])
        else:
            big_median_index = (median_index[0] - left_small_cursor - 1, median_index[1] - left_small_cursor - 1)
            median_el = (big[big_median_index[0]], big[big_median_index[1]])

        return (median_el, median_index)

    def binarySearch(self, A, p, r, el):
        while p <= r:
            m = int((r + p) / 2)
            if A[m] == el:
                return True, m, m, m
            elif A[m] > el:
                r = m - 1
                left = r
                right = m
            else:
                p = m + 1
                left = m
                right = p
        return False, m, left, right

    def biggest(self, num1, num2):
        return num1 if num1 > num2 else num2

    def checkMedianSortedArrays(self, nums1, nums2):
        if len(nums1) + len(nums2) == 0:
            return
        res = self.findMedianSortedArrays_(self, nums1, nums2)
        sortedArr = sorted(nums1 + nums2)
        expectedMedian = sortedArr[res[1][0]], sortedArr[res[1][1]]
        print("---------")
        print("nums1 = " + nums1.__repr__() + ", nums2 = " + nums2.__repr__() + ", Sorted = " + sortedArr.__repr__())
        print('Median: ' + res[1].__repr__(), ', Result: ' + res[0].__repr__(),
              ', Expected: ' + expectedMedian.__repr__())

        assert expectedMedian == res[0]

    def binarySearch_(A, el):
        return Solution.binarySearch(A, 0, len(A) - 1, el)


def customTest():
    Solution.checkMedianSortedArrays(Solution, nums1=[1, 1, 1, 1, 1, 100, 100, 100], nums2=[20, 20, 20, 30, 30])
    Solution.checkMedianSortedArrays(Solution, nums1=[-30, -20, -10, -2, -1, 1, 100, 100, 100],
                                     nums2=[20, 30, 30, 10000, 10000, 10000])
    Solution.checkMedianSortedArrays(Solution, nums1=[1, 2, 5, 7, 10], nums2=[])
    Solution.checkMedianSortedArrays(Solution, nums1=[1, 2, 5, 7, 10], nums2=[-1])
    Solution.checkMedianSortedArrays(Solution, nums1=[1, 2, 5, 7, 10], nums2=[15])
    Solution.checkMedianSortedArrays(Solution, nums1=[1, 2, 5, 7, 10], nums2=[8, 9])
    Solution.checkMedianSortedArrays(Solution, nums1=[1, 2, 5, 7, 10], nums2=[15, 16])
    Solution.checkMedianSortedArrays(Solution, nums1=[1, 5, 9, 10, 15, 17, 20], nums2=[6, 11, 16])
    Solution.checkMedianSortedArrays(Solution, nums1=[0, 10, 20, 30, 40], nums2=[5, 15, 25, 35])
    Solution.checkMedianSortedArrays(Solution, nums1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 12],
                                     nums2=[15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27])
    Solution.checkMedianSortedArrays(Solution, nums1=[1, 2, 5, 7, 10], nums2=[-1, 0])
    Solution.checkMedianSortedArrays(Solution, nums1=[2, 5, 7, 10, 12, 15, 17, 20], nums2=[-1, 0, 3, 6])
    Solution.checkMedianSortedArrays(Solution, nums1=[2, 5, 7, 10, 12, 15, 17, 20], nums2=[-1, 0, 3, 8])
    Solution.checkMedianSortedArrays(Solution, nums1=[0, 1000, 1001, 1002, 1003], nums2=[500, 501, 502, 1005])
    Solution.checkMedianSortedArrays(Solution, nums1=[37, 40, 46, 83],
                                     nums2=[6, 17, 20, 35, 37, 38, 40, 46, 65, 71, 73, 82, 83, 84])
    Solution.checkMedianSortedArrays(Solution, nums1=[52, 52, 56, 70],
                                     nums2=[11, 16, 41, 42, 48, 52, 52, 56, 58, 66, 70, 75, 76, 78])
    Solution.checkMedianSortedArrays(Solution, nums1=[61, 72, 87, 90, 95, 97],
                                     nums2=[4, 13, 16, 16, 24, 29, 32, 57, 61, 72, 73, 75, 87, 90, 95, 97])


def randomTest_fixedArrayLength(test_num):
    i = 1
    while i <= test_num:
        Solution.checkMedianSortedArrays(Solution, nums1=rand_array_sorted(10, 1, 1000),
                                         nums2=rand_array_sorted(0, 50, 100))
        i = i + 1


def randomTest_randomArrayLength(test_num):
    i = 1
    stats = {}
    while i <= test_num:
        arr1 = rand_array_sorted(randint(0, 20), 1, 1000)
        arr2 = rand_array_sorted(randint(0, 10), 50, 100)

        c1 = 0 if stats.get(len(arr1)) is None else stats.get(len(arr1)) + 1
        c2 = 0 if stats.get(len(arr2)) is None else stats.get(len(arr2)) + 1
        stats[len(arr1)] = c1
        stats[len(arr2)] = c2
        Solution.checkMedianSortedArrays(Solution, nums1=arr1,
                                         nums2=arr2)
        i = i + 1

    print("stats: " + sorted(stats.items()).__repr__())


# customTest()


print(Solution.findMedianSortedArrays(Solution(),
                                 nums1=[1, 2],
                                 nums2=[3, 4]))


# [1,3]
# [2]
# [1, 2, 5, 7, 10]
# [8, 9]
# [1, 1, 1, 1, 1, 100, 100, 100]
# [20, 20, 20, 30, 30]
# [1, 2, 5, 7, 10]
# []
# [1,2]
# [3,4]
# [1,3]
# [2]

# randomTest_fixedArrayLength(1000000000000000)
# randomTest_randomArrayLength(100000000000000)
