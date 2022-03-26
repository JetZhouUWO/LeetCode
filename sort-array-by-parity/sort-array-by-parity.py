class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = [item for item in nums if item%2 == 0]
        odd = [item for item in nums if item%2 == 1]
        return even + odd
        