class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # m = len(grid)
        # n = len(grid[0])
        # def minpath(i, j, s):
        #     # Out of bounds
        #     if i >= m or j >= n:
        #         return float('inf')
            
        #     # If we reach bottom-right cell, include its value and return
        #     if i == m - 1 and j == n - 1:
        #         return s + grid[i][j]
            
        #     # Move right or down
        #     return min(
        #         minpath(i + 1, j, s + grid[i][j]),  # move down
        #         minpath(i, j + 1, s + grid[i][j])   # move right
        #     )

        # return minpath(0, 0, 0)


        m = len(grid)
        n = len(grid[0])
        dp=[[None for i in range(n)] for j in range(m)]
        def minpath(i, j, ):
            # Out of bounds
            if i >= m or j >= n:
                return float('inf')
            # If we reach bottom-right cell, include its value and return
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            if dp[i][j] is not None:
                return dp[i][j]
             # Move down or right
            down = minpath(i + 1, j)
            right = minpath(i, j + 1)

            dp[i][j] = grid[i][j] + min(down, right)
            return dp[i][j]

        return minpath(0, 0)
            
