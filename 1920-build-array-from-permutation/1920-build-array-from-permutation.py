class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(n) solution
        rst = []
        i = 0
        while i < len(nums):
            rst.append(nums[nums[i]])
            i+=1
        return rst
    
        # O(1) solution
        i = 0
        while i < len(nums):
            nums[i],nums[nums[i]] = nums[nums[i]], nums[i]
            i+=1
        return nums
        