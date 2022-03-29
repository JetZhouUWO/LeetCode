class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = []
        i = 0
        while i < len(nums):
            rst.append(nums[nums[i]])
            i+=1
        return rst
        