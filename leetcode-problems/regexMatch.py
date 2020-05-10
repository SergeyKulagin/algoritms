class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx = 0
        p_idx = 0
        s_len = len(s)
        p_len = len(p)
        while s_idx < s_len and p_idx < p_len:
            if p[p_idx] == '.':
                s_idx += 1
                p_idx += 1
            elif p[p_idx] == '*':
                if p_idx == 0:
                    raise RuntimeError('Invalid pattern detected')
                elif p[p_idx - 1] == '.' or p[p_idx - 1] == s[s_idx]:
                    s_idx += 1
                else:
                    p_idx += 1
            else:
                if s[s_idx] == p[p_idx]:
                    s_idx += 1
                    p_idx += 1
                elif p_idx + 1 < p_len and p[p_idx + 1] == '*':
                    p_idx += 2
                else:
                    return False

        return True if (s_idx >= s_len and p_idx >= p_len - 1) else False


s = Solution()
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("mississippi", "mis*is*p*."))
