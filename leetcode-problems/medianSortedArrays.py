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
            if cur_idx < median_index[0]:
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
        else:
            big_median_index = (median_index[0] - left_small_cursor - 1, median_index[1] - left_small_cursor - 1)
            median_el = (big[big_median_index[0]], big[big_median_index[1]])

        print(median_el)
        # what to do next?

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
# Solution.findMedianSortedArrays(Solution, nums1=[1,2,5,7,10], nums2=[8,9])
# Solution.findMedianSortedArrays(Solution, nums1=[1,2,5,7,10], nums2=[15,16])
# Solution.findMedianSortedArrays(Solution, nums1=[1,5,9,10,15,17,20], nums2=[6,11,16])
# Solution.findMedianSortedArrays(Solution, nums1=[0,10,20,30,40], nums2=[5,15,25,35])
Solution.findMedianSortedArrays(Solution, nums1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 12], nums2=[15, 16, 17, 18, 19, 21, 22,23,24, 25,26, 27])
