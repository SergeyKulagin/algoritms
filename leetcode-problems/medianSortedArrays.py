from util import rand_array_sorted

# todo in progress
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        (small, big) = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        full_len = len(nums1) + len(nums2)
        median_index = (int(full_len / 2) - 1, int(full_len / 2)) if full_len % 2 == 0 else (
            int(full_len / 2), int(full_len / 2))
        if len(small) == 0:
            return (big[median_index[0]] + big[median_index[1]]) / 2

        p = 0
        r = len(small) - 1
        left_big_cursor = None
        while p <= r:
            m = int((p + r) / 2)
            res = Solution.binarySearch(big, 0, len(big) - 1, small[m])
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
                median_el = (
                    big[median_index[0]], big[median_index[1]] if median_index[0] == median_index[1] else small[0])
            else:
                median_el = (small[median_index[0] - len(big)], small[median_index[1] - len(big)])
        elif left_big_cursor + left_small_cursor + 1 == median_index[0]:
            median_el = (small[left_small_cursor],
                         small[left_small_cursor] if median_index[0] == median_index[1] else big[left_big_cursor + 1])
        elif left_big_cursor + left_small_cursor + 1 == median_index[1]:
            median_el = (small[left_small_cursor] if median_index[0] == median_index[1] else big[left_big_cursor],
                         small[left_small_cursor])
        else:
            big_median_index = (median_index[0] - left_small_cursor - 1, median_index[1] - left_small_cursor - 1)
            median_el = (big[big_median_index[0]], big[big_median_index[1]])

        return (median_el, median_index)


    def checkMedianSortedArrays(self, nums1, nums2):
        res = self.findMedianSortedArrays(self, nums1, nums2)
        sortedArr = sorted(nums1 + nums2)
        expectedMedian = sortedArr[res[1][0]], sortedArr[res[1][1]]
        print("---------")
        print("nums1 = " + nums1.__repr__() + ", nums2 = " + nums2.__repr__() + ", Sorted = " + sortedArr.__repr__())
        print('Median: ' + res[1].__repr__(), ', Result: ' + res[0].__repr__(), ', Expected: ' + expectedMedian.__repr__())

        assert expectedMedian == res[0]

    def binarySearch(A, p, r, el):
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

    def binarySearch_(A, el):
        return Solution.binarySearch(A, 0, len(A) - 1, el)


# print(Solution.binarySearch_([1, 3, 5, 10], 7))
# print(Solution.binarySearch_([1, 3, 5, 10], 2))
# print(Solution.binarySearch_([1, 3, 5, 10], -1))
# print(Solution.binarySearch_([1, 3, 5, 10], 3))
# print(Solution.binarySearch_([1, 3, 5, 10], 12))
# Solution.checkMedianSortedArrays(Solution, nums1=[1,2,5,7,10], nums2=[8,9])
# Solution.checkMedianSortedArrays(Solution, nums1=[1,2,5,7,10], nums2=[15,16])
# Solution.checkMedianSortedArrays(Solution, nums1=[1,5,9,10,15,17,20], nums2=[6,11,16])
# Solution.checkMedianSortedArrays(Solution, nums1=[0,10,20,30,40], nums2=[5,15,25,35])
# Solution.checkMedianSortedArrays(Solution, nums1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 12], nums2=[15, 16, 17, 18, 19, 21, 22,23,24, 25,26, 27])
# Solution.checkMedianSortedArrays(Solution, nums1=[1,2,5,7,10], nums2=[-1,0])
# Solution.checkMedianSortedArrays(Solution, nums1=[2, 5, 7, 10, 12, 15, 17, 20], nums2=[-1, 0, 3, 6])
# Solution.checkMedianSortedArrays(Solution, nums1=[2, 5, 7, 10, 12, 15, 17, 20], nums2=[-1, 0, 3, 8])
# Solution.checkMedianSortedArrays(Solution, nums1=[0, 1000, 1001, 1002, 1003], nums2=[500, 501, 502, 1005])
Solution.checkMedianSortedArrays(Solution, nums1=rand_array_sorted(10, 1, 100), nums2=rand_array_sorted(4, 1, 100))


# PROBLEM 1
# nums1 = [6, 17, 20, 35, 38, 65, 71, 73, 82, 84], nums2 = [37, 40, 46, 83], Sorted = [6, 17, 20, 35, 37, 38, 40, 46, 65, 71, 73, 82, 83, 84]
# Median: (6, 7) , Result: (38, 46) , Expected: (40, 46)
