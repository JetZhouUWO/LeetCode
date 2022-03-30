class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        rst = sorted(str(num))
        return int(rst[0]+rst[2]) + int(rst[1]+rst[3])
