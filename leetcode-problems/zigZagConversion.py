class Solution(object):
    def convert(self, s, numRows):
        if numRows == 0 or numRows == 1:
            return s
        i = 0
        n = len(s)
        zigZag = ["x"] * n
        step = 2 * numRows - 2
        zIdx = 0
        while i < numRows:
            if i >= n: break
            stepBack = 2 * i
            j = i
            zigZag[zIdx] = s[j]
            j += step
            while j - stepBack < n:
                if 0 < i < numRows - 1:
                    zIdx += 1
                    zigZag[zIdx] = s[j - stepBack]
                if j < n:
                    zIdx += 1
                    zigZag[zIdx] = s[j]
                j += step
            zIdx += 1
            i += 1
        return ''.join(zigZag)


s = Solution()
print(s.convert("PAYPALISHIRING", 1))
print(s.convert("PAYPALISHIRING", 2))
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
print(s.convert("PAYPALISHIRING", 5))
print(s.convert("PAYPALISHIRING", 6))
print(s.convert("A", 3))
print(s.convert("AB", 5))


# "PAYPALISHIRING"
# 1
# "PAYPALISHIRING"
# 0
# "PAYPALISHIRING"
# 2
# "PAYPALISHIRING"
# 3
# "PAYPALISHIRING"
# 4
# "PAYPALISHIRING"
# 5
# "PAYPALISHIRING"
# 6
# "PAYPALISHIRING"
# 100
# "A"
# 2
