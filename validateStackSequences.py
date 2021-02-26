from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        tstack = []  # test stack
        while (len(pushed) > 0):
            tstack.append(pushed[0])
            pushed = pushed[1:]
            while tstack and tstack[-1] == popped[0]:
                tstack.pop()
                popped = popped[1:]
        if len(popped) > 0:
            return False
        return True


soln = Solution()
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
# pushed = [1, 2, 3, 4, 5]
# popped = [4, 3, 5, 1, 2]
print(soln.validateStackSequences(pushed, popped))
