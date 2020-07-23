# see also https://regex101.com/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx = 0
        p_idx = 0
        s_len = len(s)
        p_len = len(p)
        p_context_cur = self.get(p, 0)
        p_context_prev = None
        while s_idx < s_len and p_context_cur is not None:
            if p_context_cur == '.':
                p_idx += 1
                s_idx += 1
                p_context_prev = p_context_cur
                p_context_cur = self.get(p, p_idx)
            elif p_context_prev == '.' and p_context_cur == '*':  # handling '.*'
                while self.get(p, p_idx + 1) == '.' and self.get(p, p_idx + 2) == '*':
                    p_idx += 2
                while self.get(p, p_idx + 1) == '.':
                    p_idx += 1

                p_idx += 1
                if self.get(p, p_idx) == s[s_idx]:
                    p_idx += 1
                    s_idx += 1
                    p_context_cur = self.get(p, p_idx)
                    p_context_prev = self.get(s, s_idx)
                else:
                    s_idx += 1
            elif p_context_cur == '*':
                if p_idx == 0 or p_context_prev == '*':
                    raise RuntimeError('Invalid pattern')
                elif p_context_prev == s[s_idx]:
                    s_idx += 1
                else:
                    p_idx += 1
                    p_context_prev = '*'
                    p_context_cur = self.get(p, p_idx)
            else:
                if s[s_idx] == p_context_cur:
                    s_idx += 1
                    p_idx += 1
                    p_context_prev = p_context_cur
                    p_context_cur = self.get(p, p_idx)
                elif self.get(p, p_idx + 1) == '*':
                    p_idx += 2
                    p_context_prev = '*'
                    p_context_cur = self.get(p, p_idx)
                else:
                    return False

        return s_idx >= s_len and (p_idx >= p_len - 1 or self.emptyExpressionLeft(p, p_idx, len(p)))

    def get(self, arr, i):
        if len(arr) > i: return arr[i]

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
s.isMatchWithPrint("1", '1*')
s.isMatchWithPrint("1", '1.*')
s.isMatchWithPrint("aa", "a")
s.isMatchWithPrint("aa", "a*")
s.isMatchWithPrint("ab", ".*")
s.isMatchWithPrint("aab", "c*a*b")
s.isMatchWithPrint("mississippi", "mis*is*p*.")
s.isMatchWithPrint("aaaaaaaaaaaaabq", ".*.q")
s.isMatchWithPrint("abc", ".*.*.*")
s.isMatchWithPrint("hello", ".*")
