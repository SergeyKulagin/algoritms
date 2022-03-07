# todo fix it!

class Solution:
    def insertionSortAsc(self, a):
        for j in range(1, len(a)):
            key = a[j]
            i = j - 1
            while i >= 0 and a[i] > key:
                a[i + 1] = a[i]
                i = i - 1
            a[i + 1] = key
        return a

    def binarySearchInAsc(self, a, el, left):
        right = len(a)

        while right > left:
            mid = int((left + right) / 2)
            if a[mid] == el:
                return mid

            if el > a[mid]:
                left = mid + 1
            else:
                right = mid

        return None

    def threeSum(self, a):
        res = []
        b = self.insertionSortAsc(a.copy())
        sign_change_idx = 0
        # middle_dx = int(len(a) / 2)
        for i in range(0, len(b)):
            if b[i] >= 0:
                sign_change_idx = i
                break
        # if sign_change_idx > middle_dx:
        #     b.reverse()

        b_prev = None
        for i in range(0, sign_change_idx):
            if b[i] == b_prev:
                continue
            for j in range(i + 1, len(b)):
                two_sum = b[i] + b[j]
                third = self.binarySearchInAsc(b, -two_sum, max(sign_change_idx, j + 1))
                if third is not None:
                    res.append([b[i], b[j], b[third]])
            b_prev = b[i]

        print("expected= " + str(self.threeSumFullSearch(a)) + ", real = " + str(res))
        return res

    def threeSumFullSearch(self, x):
        res = []
        a = x.copy()
        self.insertionSortAsc(a)

        i_prev = None
        j_prev = None
        k_prev = None
        for i in range(0, len(a)):
            if a[i] == i_prev:
                continue
            for j in range(i + 1, len(a)):
                if a[j] == j_prev:
                    continue
                for k in range(j + 1, len(a)):
                    if a[k] == k_prev:
                        continue
                    if a[i] + a[j] + a[k] == 0:
                        res.append([a[i], a[j], a[k]])
                    k_prev = a[k]
                j_prev = a[j]
            i_prev = a[i]
        return res


s = Solution()
# s.threeSum([-1, 0, 1, 2, -1, -4])
s.threeSum([1, 1, 1, 1, 0, 0, 0, -1, -1, -1, -1])
# s.threeSum([0])
# s.threeSum([])
