# see also https://regex101.com/

import re


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

                if self.get(p, p_idx + 1) is None:
                    return True

                s_back = s_len - 1  # go backward for search for last inclusion
                found = False
                while s_back >= s_idx:
                    if self.get(p, p_idx + 1) == s[s_back]:
                        p_idx += 2
                        s_idx = s_back + 1
                        p_context_cur = self.get(p, p_idx)
                        p_context_prev = self.get(s, s_back)
                        found = True
                        break
                    else:
                        s_back -= 1
                if not found:
                    return False
            elif p_context_cur == '*':
                if p_context_prev is None or p_context_prev == '*':
                    raise RuntimeError(f'Invalid pattern {p}')
                elif p_context_prev == s[s_idx]:
                    while self.get(p, p_idx + 1) == p_context_prev:
                        p_idx += 2
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

        return s_idx >= s_len and (p_idx >= p_len or self.emptyExpressionLeft(p, p_idx))

    def get(self, arr, i):
        if len(arr) > i: return arr[i]

    def emptyExpressionLeft(self, p: str, p_idx: int):
        p_len = len(p)
        p_cur = p[p_idx]
        p_prev = self.get(p, p_idx - 1)
        while p_idx < p_len:
            if p_cur == '*':
                if p_prev == '*':
                    raise RuntimeError(f'Invalid pattern {p}')
                p_prev = p_cur
                p_idx += 1
                p_cur = self.get(p, p_idx)
            else:
                if self.get(p, p_idx + 1) == '*':
                    p_prev = p_cur
                    p_idx += 1
                    p_cur = '*'
                else:
                    return False
        return True

    def isMatchWithPrint(self, s: str, p: str) -> bool:
        match = self.isMatch(s, p)

        # print(s + " is mathes to " + p + " = " + str(match))
        print('"' + s + '"')
        print('"' + p + '"')
        assert match == bool(re.fullmatch(p, s)), "Not expected"


s = Solution()
#exact match
s.isMatchWithPrint("abc", "abc")
s.isMatchWithPrint("abc", "abcc")
s.isMatchWithPrint("abcd", "abc")
s.isMatchWithPrint("a", "")
s.isMatchWithPrint("", "a")
# expressions (star)
s.isMatchWithPrint("a", 'a*')
s.isMatchWithPrint("aaaaa", 'a*')
s.isMatchWithPrint("aaaaa", 'a*a*')
s.isMatchWithPrint("aaaaa", 'a*a*a*a*a*')
s.isMatchWithPrint("aaaaa", 'b*')
s.isMatchWithPrint("aab", "c*a*b")
# expressions (dot)
s.isMatchWithPrint("a", ".")
s.isMatchWithPrint("a", "..")
s.isMatchWithPrint("a", "a.")
s.isMatchWithPrint("a", "a..")
s.isMatchWithPrint("aaa", "...")
s.isMatchWithPrint("aaa", "....")
s.isMatchWithPrint("aaa", ".a.")
# expressions (dot and match)
s.isMatchWithPrint("1", '1.*')
s.isMatchWithPrint("1", '1.*.*.*')
s.isMatchWithPrint("1", '1.*.*.')
s.isMatchWithPrint("1", '1.*.*.')
s.isMatchWithPrint("1b1", '1.*.*1')
s.isMatchWithPrint("1b1c1", '1.*.*1')
s.isMatchWithPrint("1b1c1", '1.*.*1')
s.isMatchWithPrint("1b1sadfsafsdfasc1", '.*')

# misc
s.isMatchWithPrint("mississippi", "mis*is*p*.")
s.isMatchWithPrint("aaaaaaaaaaaaabq", ".*.q")
s.isMatchWithPrint("abc", ".*.*.*")
s.isMatchWithPrint("hello", ".*")
s.isMatchWithPrint("", "")
s.isMatchWithPrint("", ".*")
s.isMatchWithPrint("qqwqrwe", ".*")
s.isMatchWithPrint("dsfsdsafdfd", ".*a.*")
s.isMatchWithPrint("dsfsdsfdfd", ".*a.*")
s.isMatchWithPrint("aaabbbccca", "a.*b")
s.isMatchWithPrint("aaabbbccca", "a.*")
s.isMatchWithPrint("aaabbbccca", "a.*a")
s.isMatchWithPrint("aaa", "a*a")
s.isMatchWithPrint("aaa", "ab*a*c*a")
