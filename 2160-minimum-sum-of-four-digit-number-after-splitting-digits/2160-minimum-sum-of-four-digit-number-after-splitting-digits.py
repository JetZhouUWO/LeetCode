class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        rst = sorted(str(num))
        num1 = rst[0]+rst[2]
        num2 = rst[1]+rst[3]
        return int(num1) + int(num2)
        