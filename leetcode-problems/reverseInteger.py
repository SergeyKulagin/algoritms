from random import *

# 2^31 - 1 = 2147483647
# -2^31 = -2147483648
intmax = 2147483647
intmin = -2147483648

class Solution:

    def reverse(self, x: int) -> int:
        if x == intmin:
            return 0  # eliminate corner case overflow
        sign = -1 if x < 0 else 1
        x = sign * x
        overflowDigits = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7 if sign > 0 else 8]
        digits = [None] * 10
        place = 10
        prevRemains = 0
        remains = None
        digitCursor = -1
        while remains != x:
            digitCursor += 1
            prevPlace = int(place / 10)
            remains = (x % place)
            digit = int((remains - prevRemains) / prevPlace)
            digits[digitCursor] = digit
            prevRemains = remains
            place *= 10

        place = 1
        num = 0
        overflowPossible = False
        overflowCursor = len(overflowDigits) - 1
        while digitCursor >= 0:
            digit = digits[digitCursor]
            num = num + digit * place
            place *= 10
            digitCursor -= 1
            if digit > overflowDigits[overflowCursor]:
                overflowPossible = True
            elif digit < overflowDigits[overflowCursor]:
                overflowPossible = False
            overflowCursor -= 1

        if overflowCursor == -1 and overflowPossible:
            num = 0
        else:
            num = num * sign
        return num

    def reverseTest(self, x: int) -> int:
        if x == 0: return 0
        s = str(x)
        neg = (s[0] == '-')
        s = s[1:len(s)] if neg else s[0:len(s)]
        rev = s[len(s)::-1].lstrip("0")
        return int(rev) * -1 if neg else int(rev)

    def reverseCompare(self, x: int) -> int:
        expected = self.reverseTest(x)
        overflow = self.isOverflow(expected)
        actual = self.reverse(x)
        res = x, actual, expected, overflow
        if overflow:
            assert actual == 0, "expect 0 for overflow, but actual=" + str(actual)
        else:
            assert actual == expected, "actual=" + str(actual) + ", expected=" + str(expected)
        return res

    def allRangeTest(self):
        end = intmax + 10
        i = intmin - 10
        while i < end:
            print(self.reverseCompare(i))
            i += 1

    def randomTest(self):
        num = 1000000
        i = 0
        while i < num:
            print(self.reverseCompare(randint(intmin - 1000, intmax + 1000)))
            i += 1

    def isOverflow(self, rev: int) -> bool:
        return True if rev > intmax or rev < intmin else False


s = Solution()
# print(s.reverseCompare(-34556))
# print(s.reverseCompare(12345678))
# print(s.reverseCompare(100101))
# print(s.reverseCompare(1112345678))
# print(s.reverseCompare(-34556))
# print(s.reverseCompare(intmax))
# print(s.reverseCompare(intmin))
# s.allRangeTest()
# s.randomTest()
s.reverse(65777777777777756)
