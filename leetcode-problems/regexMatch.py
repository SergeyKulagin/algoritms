# see also https://regex101.com/

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
                    raise RuntimeError('Invalid pattern')
                elif p[p_idx - 1] == '.':
                    if p_idx < p_len - 1 and p[p_idx + 1] == s[s_idx]:
                        s_idx += 1
                        p_idx += 1
                    # elif p_idx < p_len - 1 and p[p_idx + 1] == '.':
                    #     p_idx += 1
                    else:
                        s_idx += 1
                elif p[p_idx - 1] == s[s_idx]:
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

        return s_idx >= s_len and (p_idx >= p_len - 1 or self.emptyExpressionLeft(p, p_idx, len(p)))

    def emptyExpressionLeft(self, p: str, start: int, end: int):
        while start < end:
            if p[start] == '*':
                if p[start - 1] == '*':
                    raise RuntimeError('Invalid pattern')
                start += 1
            elif start < end - 1 and p[start + 1] == '*':
                start += 1
            else:
                return False

    def isMatchWithPrint(self, s: str, p: str) -> bool:
        print(s + " is mathes to " + p + " = " + str(self.isMatch(s, p)))


s = Solution()
# s.isMatchWithPrint("1", '1*')
# s.isMatchWithPrint("1", '1.*')
# s.isMatchWithPrint("aa", "a")
# s.isMatchWithPrint("aa", "a*")
# s.isMatchWithPrint("ab", ".*")
# s.isMatchWithPrint("aab", "c*a*b")
# s.isMatchWithPrint("mississippi", "mis*is*p*.")
s.isMatchWithPrint("aaaaaaaaaaaaabq", ".*.q")
# s.isMatchWithPrint("abc", ".*.*.*")
# s.isMatchWithPrint("hello", ".*")
