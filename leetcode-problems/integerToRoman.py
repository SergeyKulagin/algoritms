mapping = {
    1: {
        1: 'I',
        5: 'V'
    },
    10: {
        1: 'X',
        5: 'L'
    },
    100: {
        1: 'C',
        5: 'D'
    },
    1000: {
        1: 'M'
    }
}


class Solution:
    def intToRoman(self, num: int) -> str:
        assert 1 <= num <= 3999
        res = ""
        pos = 1
        leftover = None
        while leftover != num:
            leftover = num % (pos * 10)
            digit = int(leftover / pos)
            res = self.digitToRoman(pos, digit) + res
            pos *= 10

        return res

    def digitToRoman(self, pos: int, digit: int):
        if digit == 0:
            return ""
        if 1 <= digit <= 3:
            return mapping[pos][1] * digit
        if digit == 4:
            return mapping[pos][1] + mapping[pos][5]
        if digit == 5:
            return mapping[pos][5]
        if 6 <= digit <= 8:
            return mapping[pos][5] + mapping[pos][1] * (digit - 5)
        if digit == 9:
            return mapping[pos][1] + mapping[pos * 10][1]


s = Solution();
for i in range(1, 4000):
    print(str(i) + "=" + s.intToRoman(i))

# floor(12345 % 100 / 10)

#    Symbol       Value
#    I             1
#    V             5
#    X             10
#    L             50
#    C             100
#    D             500
#    M             1000

# num = 1994 => MCMXCIV
