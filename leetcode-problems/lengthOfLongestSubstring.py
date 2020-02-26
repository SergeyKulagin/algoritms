class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = 0
        n = len(s)
        p = 0
        max_len = 0
        cur_len = 0
        while i < n:
            j = i - 1
            while j > p - 1:
                if s[j] == s[i]:
                    p = j + 1  # start counting from new position
                    max_len = max_len if max_len > cur_len else cur_len
                    cur_len = i - j
                    j = p + 1  # to avoid cur_len increment on this iteration
                    break
                j = j - 1

            if j < p:
                cur_len = cur_len + 1
            i = i + 1

        return max_len if max_len > cur_len else cur_len

    def lengthOfLongestSubstring_(s):
        return s, Solution.lengthOfLongestSubstring(None, s)


print(Solution.lengthOfLongestSubstring_(""))
print(Solution.lengthOfLongestSubstring_("a"))
print(Solution.lengthOfLongestSubstring_("pwwkew"))
print(Solution.lengthOfLongestSubstring_("sergeyvorobey"))
print(Solution.lengthOfLongestSubstring_("aaaaabbbbcccc"))
print(Solution.lengthOfLongestSubstring_("abccccaabc"))
print(Solution.lengthOfLongestSubstring_("eabcdefe"))
print(Solution.lengthOfLongestSubstring_("aa"))
print(Solution.lengthOfLongestSubstring_("aaa"))
print(Solution.lengthOfLongestSubstring_("aaab"))
print(Solution.lengthOfLongestSubstring_("aaab"))
print(Solution.lengthOfLongestSubstring_("bbbbbb"))
print(Solution.lengthOfLongestSubstring_("helzmlouw"))