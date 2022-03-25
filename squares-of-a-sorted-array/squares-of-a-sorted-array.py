class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # rst = [item**2 for item in nums]
        # sorted(item**2 for item in nums)
        return sorted(item**2 for item in nums) #sorted(rst)