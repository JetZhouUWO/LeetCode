class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Method does not work due to time limit exceeded
        # if n <= 3:
        #     return n
        # else: return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
        