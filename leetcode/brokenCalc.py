class Solution(object):
    def brokenCalcSLOW(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        inc = 0
        while X != Y:
            if Y % 2 == 1 or X > Y:
                Y += 1
            else:
                Y /= 2
            inc += 1
        return inc

    def brokenCalc(self, X, Y):
        inc = 0
        while Y > X:
            inc += 1
            if Y % 2:
                Y += 1
            else:
                Y /= 2
        return inc + X-Y


sol = Solution()
print(sol.brokenCalc(1000000000, 1))
