def add(a: int, b: int) -> int:
    return a+b


class Solution:
    def minOperations(self, boxes: str) -> str:
        init = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                init.append(i)
        ans = []
        for i in range(len(boxes)):
            moves = 0
            for j in init:
                moves += abs(i-j)
            ans.append(moves)
        return ans


soln = Solution()
print(soln.minOperations('0'))
