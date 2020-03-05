# todo in progress
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        p1 = 0
        r1 = len(nums1) - 1
        p2 = 0
        r2 = len(nums2) - 1

        while True:
            if r1 > p1 and r2 > p2:
                break

            if r1 > p1:
                m1 = int(r1 - p1) / 2
            if r2 > p2:
                m2 = int(r2 - p2) / 2

            if nums1[m1] == nums2[m2]:
                break
            elif nums1[m1] < nums2[m2]:
                p1 = m1 + 1
                r2 = m2 - 1
            else:
                r1 = m1 - 1
                p2 = m2 + 1
