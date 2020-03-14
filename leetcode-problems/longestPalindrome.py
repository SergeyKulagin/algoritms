def longestPalindrome(s):
    n = len(s) - 1
    r = n
    while r > 0:
        i = 0
        j = r
        while j <= n:
            print("Check " + s[i:j + 1])
            palindrome = isPalindrome(s, i, j)
            if palindrome:
                return (i, j), s[i:j + 1]
            i = i + 1
            j = j + 1
        r = r - 1
    return 0, s[0]


def isPalindrome(s, p, r):
    i = p
    j = r
    while i <= r:
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
