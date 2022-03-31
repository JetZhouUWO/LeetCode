class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Method does not work due to time limit exceeded (应该是可以用的)
        # if n <= 3:
        #     return n
        # else: return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        # O(n) space答案
        # if n == 1:
        #     return 1
        # res = [0 for i in range(n)] # [0 for i in xrange(n)]
        # res[0], res[1] = 1, 2
        # for i in range(2, n): # for i in xrange(2, n)
        #     res[i] = res[i-1] + res[i-2]
        # return res[-1]
    
        # constant space answer
        if n == 1:
            return 1
        a,b = 1,2
        for _ in range(2,n):
            tmp = b
            b = a+b
            a=tmp
        return b
        