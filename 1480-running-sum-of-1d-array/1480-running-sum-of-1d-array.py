class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = nums[0]
        i = 1
        while i < len(nums):
            nums[i] = total + nums[i]
            total = nums[i]
            i+=1
        return nums