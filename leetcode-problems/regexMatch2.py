# see also https://regex101.com/

import re


def build_regex(p):
    regex = []
    p_len = len(p)
    i = 0
    while i < p_len:
        if i + 1 < p_len and p[i + 1] == '*':
            assert p[i] != '*'
            regex.append((p[i], '*'))
            i += 2
        else:
            assert p[i] != '*'
            regex.append((p[i], '1'))
            i += 1
    return regex


def find_possibilities(idx, regex):
    pos = []
    i = idx
    while i < len(regex):
        if regex[i][1] == '*':
            pos.append((i, regex[i]))
            i += 1
        else:
            pos.append((i, regex[i]))
            break
    return pos


def optional_left(regex, idx):
    while idx < len(regex):
        if regex[idx][1] != '*':
            return False
        idx += 1
    return True


class Solution:
    def isMatch(self, s: str, p: str):
        s_idx = 0
        regex_max_idx = -1
        regex = build_regex(p)  # a*b => [(a, *), (b, 1)]
        possibilities = find_possibilities(0, regex)
        while s_idx < len(s):
            possibility_idx = 0
            next_possibilities = []
            symbol_match = False
            while possibility_idx < len(possibilities):
                possibility_global_idx = possibilities[possibility_idx][0]
                possibility_symbol = possibilities[possibility_idx][1][0]
                possibility_control = possibilities[possibility_idx][1][1]

                if possibility_symbol == s[s_idx] or possibility_symbol == '.':
                    symbol_match = True
                    last_symbol = s_idx == len(s) - 1
                    regex_max_idx = possibility_global_idx if possibility_global_idx > regex_max_idx and last_symbol else regex_max_idx
                    if possibility_control == '*':
                        next_possibilities.extend(find_possibilities(possibility_global_idx, regex))
                    else:
                        next_possibilities.extend(find_possibilities(possibility_global_idx + 1, regex))
                possibility_idx += 1

            if symbol_match:
                s_idx += 1
            if len(next_possibilities) == 0:
                break
            possibilities = next_possibilities

        match = s_idx == len(s) and (regex_max_idx == len(regex) - 1 or optional_left(regex, regex_max_idx + 1))
        # print(f's={s}, p={p}, s_idx={s_idx}, regex_max_idx={regex_max_idx}, match={match}')
        return match

    def is_match_print(self, s: str, p: str) -> bool:
        match = self.isMatch(s, p)

        # print(s + " is mathes to " + p + " = " + str(match))
        print('"' + s + '"')
        print('"' + p + '"')
        assert match == bool(re.fullmatch(p, s)), "Not expected"


s = Solution()
# # #exact match
# s.is_match_print("abc", "abc")
# s.is_match_print("abc", "abcc")
# s.is_match_print("abcd", "abc")
# s.is_match_print("a", "")
# s.is_match_print("", "a")
# # expressions (star)
# s.is_match_print("a", 'a*')
# s.is_match_print("aaaaa", 'a*')
# s.is_match_print("aaaaa", 'a*a*')
# s.is_match_print("aaaaa", 'a*a*a*a*a*')
# s.is_match_print("aaaaa", 'b*')
# s.is_match_print("aab", "c*a*b")
# # # expressions (dot)
# s.is_match_print("a", ".")
# s.is_match_print("a", "..")
# s.is_match_print("a", "a.")
# s.is_match_print("a", "a..")
# s.is_match_print("aaa", "...")
# s.is_match_print("aaa", "....")
# s.is_match_print("aaa", ".a.")
# # #expressions (dot and match)
# s.is_match_print("1", '1.*')
# s.is_match_print("1", '1.*.*.*')
# s.is_match_print("1", '1.*.*.')
# s.is_match_print("1", '1.*.*.')
# s.is_match_print("1b1", '1.*.*1')
# s.is_match_print("1b1c1", '1.*.*1')
# s.is_match_print("1b1c1", '1.*.*1')
# s.is_match_print("1b1sadfsafsdfasc1", '.*')
#
# # misc
# s.is_match_print("mississippi", "mis*is*p*.")
# s.is_match_print("aaaaaaaaaaaaabq", ".*.q")
# s.is_match_print("abc", ".*.*.*")
# s.is_match_print("hello", ".*")
# s.is_match_print("", "")
# s.is_match_print("", ".*")
# s.is_match_print("qqwqrwe", ".*")
# s.is_match_print("dsfsdsafdfd", ".*a.*")
# s.is_match_print("dsfsdsfdfd", ".*a.*")
# s.is_match_print("aaabbbccca", "a.*b")
# s.is_match_print("aaabbbccca", "a.*")
# s.is_match_print("aaabbbccca", "a.*a")
# s.is_match_print("aaa", "a*a")
# s.is_match_print("aaa", "ab*a*c*a")
# s.is_match_print("aaaa", "a*aaaa")
# s.is_match_print("aaaa", "a*aa")
# s.is_match_print("aaaa", "a*a*a")
# s.is_match_print("aaaa", "a*a*aa")
# s.is_match_print("aaaa", "a*a*a*aaaaa")


# time limit
s.is_match_print("aaaaaaaaaaaaab",
                 "a*a*a*a*a*a*a*a*a*a*a*a*b")
