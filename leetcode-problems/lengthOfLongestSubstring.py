# todo double-check, improve logic
class Solution(object):
    def lengthOfLongestSubstring(s):
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
                    cur_len = i - p + 1
                    j = p + 1 # to not increment cur_len
                    break
                j = j - 1

            if j <= p:
                cur_len = cur_len + 1
            i = i + 1

        return max_len if max_len > cur_len else cur_len


#print(Solution.lengthOfLongestSubstring(""))
#print(Solution.lengthOfLongestSubstring("a"))
print(Solution.lengthOfLongestSubstring("pwwkew"))
