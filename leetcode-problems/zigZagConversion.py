class Solution(object):
    def convert(self, s, numRows):
        i = 0
        n = len(s)
        zigZag = ["x"] * n
        step = 2 * numRows - 2
        zIdx = 0
        while i < numRows:
            stepBack = 2 * i
            j = i
            zigZag[zIdx] = s[j]
            j +=step
            while j < n:
                if 0 < i < numRows - 1:
                    zIdx += 1
                    zigZag[zIdx] = s[j - stepBack]
                zIdx += 1
                zigZag[zIdx] = s[j]
                j += step
            zIdx+=1
            i += 1
        return zigZag


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
