# todo in progress
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        (small, big) = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        full_len = len(nums1) + len(nums2)
        median_index = (full_len / 2, full_len / 2 - 1) if full_len % 2 == 0 else (int(full_len / 2), int(full_len / 2))
        if len(small) == 0:
            return (big[median_index[0]] + big[median_index[1]]) / 2

        left = self.binarySearch_(big, small[0])[3]
        right = self.binarySearch_(big, small[len(small) - 1])[2]

        if left > median_index[1]:
            return (big[median_index[0]] + big[median_index[1]]) / 2
        if right < median_index[0]:


    def median(A, B): #todo

    def binarySearch(A, p, r, el):
        while p <= r:
            m = int((r + p) / 2)
            if A[m] == el:
                return True, m, m - 1, m + 1
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


print(Solution.binarySearch_([1, 3, 5, 10], 7))
print(Solution.binarySearch_([1, 3, 5, 10], 2))
print(Solution.binarySearch_([1, 3, 5, 10], -1))
print(Solution.binarySearch_([1, 3, 5, 10], 3))
