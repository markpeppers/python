class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append(0)
                continue
            if stack[len(stack)-1] == 0:
                stack.pop()
                stack.append(1)
                continue
            sum = 0
            while (stack[len(stack)-1] != 0):
                sum += stack.pop()
            stack.pop()
            stack.append(2*sum)
        ans = 0
        while (len(stack) > 0):
            ans += stack.pop()
        return ans


soln = Solution()
s = ''
print(soln.scoreOfParentheses(s))
