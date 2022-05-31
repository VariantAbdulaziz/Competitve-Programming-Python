# source: https://leetcode.com/problems/range-sum-query-2d-immutable/submissions/

# strategy: prefix sum
class NumMatrix:

    def __init__(self, matrix):
        
        self.dp = [[0 for i in range(len(matrix[0]) + 1)] for i in range(len(matrix))]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r][c+1] = self.dp[r][c] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for r in range(row1, row2+1):
            ans+=(self.dp[r][col2+1] - self.dp[r][col1])
            
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)