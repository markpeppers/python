class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nums = []
        for row in matrix:
            nums.extend(row)
        return self.binarySearch(nums, target)

    def binarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if (len(nums) == 0):
            return False
        if (len(nums) == 1):
            return nums[0] == target
        pivot = len(nums) // 2
        if (target < nums[pivot]):
            return self.binarySearch(nums[:pivot], target)
        return self.binarySearch(nums[pivot:], target)


soln = Solution()
matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
print(soln.searchMatrix(matrix, 13))
print(soln.searchMatrix(matrix, 20))

matrix = [[1, 2]]
print()
print(soln.searchMatrix(matrix, 3))
print(soln.searchMatrix(matrix, 2))

matrix = [[1],
          [1]]
print()
print(soln.searchMatrix(matrix, 2))
print(soln.searchMatrix(matrix, 1))
