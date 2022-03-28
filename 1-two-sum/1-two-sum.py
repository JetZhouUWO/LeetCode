class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums):
            k = target - nums[i]
            if k in nums[i+1:]:
                #print(i+nums[i+1:].index(k))
                return [i,i + nums[i+1:].index(k) + 1]
            else: i+=1
        