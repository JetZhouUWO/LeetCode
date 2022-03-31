class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # return sum(range(len(nums)+1)) - sum(nums)
    
        return (len(nums) * (len(nums) + 1)//2) - sum(nums)
        