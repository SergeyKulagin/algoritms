import enum

space = ' '
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
plus = '+'
minus = '-'

# 2^31 - 1 = 2147483647
# -2^31 = -2147483648
intmax = 2147483647
intmin = -2147483648


class STATUS(enum.IntEnum):
    SPACE = 1,
    SIGN = 2,
    DIGIT = 3,
    SUFFIX = 4


class Solution:

    def myAtoi(self, str: str) -> int:
        size = len(str)
        i = 0
        sign = 1
        nums = []
        status = STATUS.SPACE
        while i < size:
            c = str[i]
            if c == space:
                if status == STATUS.SIGN:
                    return 0
                elif status >= STATUS.DIGIT:
                    break
            elif c == plus or c == minus:
                if status == STATUS.SPACE:
                    status = STATUS.SIGN
                    sign = -1 if c == minus else 1
                elif status == STATUS.SIGN:
                    return 0
                elif status == STATUS.DIGIT:
                    break
            elif c in digits:
                status = STATUS.DIGIT
                nums.append(int(c))
            else:
                if status == STATUS.SPACE or status == STATUS.SIGN:
                    return 0
                elif status >= STATUS.DIGIT:
                    break
            i += 1

        if len(nums) == 0:
            return 0

        res = 0
        digitCursor = len(nums) - 1
        digitMult = 1
        while digitCursor >= 0:
            res += nums[digitCursor] * digitMult
            digitMult *= 10
            digitCursor -= 1

        res = res * sign
        res = intmax if res > intmax else res
        res = intmin if res < intmin else res

        return res


s = Solution()
print(s.myAtoi("    -123{}"))
print(s.myAtoi("    123{}"))
print(s.myAtoi("    0123{}"))
print(s.myAtoi("  .  0123{}"))
print(s.myAtoi("   343434.1212"))
print(s.myAtoi("-91283472332"))
print(s.myAtoi("-912872332"))
print(s.myAtoi("+912872332"))