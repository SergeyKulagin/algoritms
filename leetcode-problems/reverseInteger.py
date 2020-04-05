class Solution:
    # 2^31 - 1 = 2147483647
    # -2^31 = -2147483648

    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = sign * x  # todo can overflowPossible?
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
        # todo double check
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
        print(num)


s = Solution()
s.reverse(12345678)
s.reverse(100101)
s.reverse(1112345678)
