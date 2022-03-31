class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        while n%3 == 0:
            n = n//3 #这个相当于loop了 #smart #如果出现了不等于0的, 然后n!=1就是不是3的倍数
        return n==1
    