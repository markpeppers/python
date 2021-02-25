from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortednums = nums.copy()
        sortednums.sort()
        leftPointer = -1
        for i in range(len(nums)):
            if nums[i] != sortednums[i]:
                leftPointer = i
                break
        if leftPointer < 0:
            return 0

        rightPointer = -1
        for i in reversed(range(len(nums))):
            if nums[i] != sortednums[i]:
                rightPointer = i
                break
        return rightPointer - leftPointer + 1


soln = Solution()
numsTests = [[2, 6, 4, 8, 10, 9, 15],
             [1, 2, 3, 4],
             [1],
             [5, 4, 3, 2, 1],
             [7, 6, 8, 9, 10],
             [1, 3, 2, 2, 2],
             [1, 3, 3, 3, 4, 2],
             [1, 3, 2, 3, 3],
             [1, 3, 5, 4, 2]]
for nums in numsTests:
    print(nums)
    print(soln.findUnsortedSubarray(nums))
    print()
