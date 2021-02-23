class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = 0, len(matrix[0]) - 1
        while (row < len(matrix) and col >= 0):
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False


soln = Solution()
matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]
print(soln.searchMatrix(matrix, 20))

matrix = [[1, 2]]
print(soln.searchMatrix(matrix, 3))
