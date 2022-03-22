class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        不考虑重复element的情况
        """
        if len(nums) == 1:
            return 0
        
        #找最大的value
        max_val = max(nums)
        #记录idx
        idx = nums.index(max_val)
        #移除最大的
        nums.remove(max_val)
        #或者用pop移除index
        #nums.pop(idx)
        if max_val >= 2*max(nums):
            return idx
        else:
            return -1
        
        