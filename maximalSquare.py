class Solution:
    def maximalSquare(self, grid):
        if not grid or not grid[0]: return 
        M, N = len(grid), len(grid[0])
        
        #we initialize another matrix (dp) with the same dimensions as the original one initialized with all 0's
        
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)] 
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]=='1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j])+1
                    ans = max(ans, dp[i+1][j+1])
        return ans**2
        
