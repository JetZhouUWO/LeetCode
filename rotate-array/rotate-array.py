class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        #index = [i in range(len(nums))]
        #index = [(i+k)%len(nums) for i in idx]
        
        temp = [0] * len(nums);
        # arr[i] should be
        # present at index[i] index
        for i in range(len(nums)):
            temp[(i+k)%len(nums)] = nums[i]
 
        # Copy temp[] to arr[]
        for i in range(len(nums)):
            nums[i] = temp[i]
        return nums
        
            