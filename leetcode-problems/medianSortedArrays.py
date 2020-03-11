# todo in progress
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        (small, big) = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        full_len = len(nums1) + len(nums2)
        median_index = (full_len / 2 - 1, full_len / 2) if full_len % 2 == 0 else (int(full_len / 2), int(full_len / 2))
        if len(small) == 0:
            return (big[median_index[0]] + big[median_index[1]]) / 2

        p = 0
        r = len(small) - 1
        while p <= r:
            m = int((p + r) / 2)
            res = Solution.binarySearch(big, 0, len(big) - 1, small[m])
            cur_idx = res[2] + m + 1
            if cur_idx < median_index[0]:
                p = m + 1
            else:
                r = m - 1

        big_cursor = res[2]
        small_cursor = m
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
#Solution.findMedianSortedArrays(Solution, nums1=[1,2,5,7,10], nums2=[8,9])
#Solution.findMedianSortedArrays(Solution, nums1=[1,2,5,7,10], nums2=[15,16])
Solution.findMedianSortedArrays(Solution, nums1=[1,5,9,10,15,17,20], nums2=[6,11,16])
