from random import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        position_mult = 1
        digits = []
        while True:
            digit = (x // position_mult) % 10
            digits.append(digit)
            position_mult *= 10
            if position_mult > x:
                break

        i = 0
        j = len(digits) - 1
        while i < j:
            if digits[i] != digits[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalindromeCheck(self, x: int):
        p = self.isPalindrome(x)
        print("Check number: " + str(x) + " is palindrome - " + str(p))
        assert self.isPalindrome(x) == self.isPalindromeTruthfull(x)


    def isPalindromeTruthfull(self, x: int)-> bool:
        xAsString = str(x)
        return xAsString == xAsString[::-1]





s = Solution()
s.isPalindromeCheck(12321)
s.isPalindromeCheck(101)
s.isPalindromeCheck(0)
s.isPalindromeCheck(-1)
s.isPalindromeCheck(-12321)
s.isPalindromeCheck(99999999)
s.isPalindromeCheck(10000000000000000000000000001)
s.isPalindromeCheck(1000000001000000001)

i = 0
while i < 1000000:
    s.isPalindromeCheck(randint(-100000000000, 10000000000))
