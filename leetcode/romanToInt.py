class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numberDict = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        curInt = 0
        prevInt = 0
        for i in range(len(s)-1, -1, -1):
            curInt = numberDict[s[i]]
            if curInt < prevInt:
                sum -= curInt
            else:
                sum += curInt
            prevInt = curInt
        return sum


soln = Solution()
tests = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV', 'MM', 'MMXXI', 'MMMCMXCIX']
for s in tests:
    print(s + ': ' + str(soln.romanToInt(s)))
