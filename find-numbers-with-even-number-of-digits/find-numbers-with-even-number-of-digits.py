class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = [len(str(x))%2 for x in nums].count(0)
        # sum(1 for x in nums if len(str(x)) % 2 == 0)
        return rst
        