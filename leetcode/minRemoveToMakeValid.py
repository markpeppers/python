class Solution(object):

    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                if len(stack) == 0:
                    s = s[:i] + '*' + s[i+1:]
                else:
                    stack.pop()
        for i in stack:
            s = s[:i] + '*' + s[i+1:]
        return s.replace('*', '')


tests = ['lee(t(c)o)de)', 'a)b(c)d', '))((', '(a(b(c)d)', '', ')d', 'hello']
sol = Solution()
for s in tests:
    print(sol.minRemoveToMakeValid(s))
