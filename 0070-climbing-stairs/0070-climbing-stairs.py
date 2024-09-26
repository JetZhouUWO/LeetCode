class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for l in range(2, n+1, 1):
            dp[l] = dp[l-1] + dp[l-2]
        return dp[-1]