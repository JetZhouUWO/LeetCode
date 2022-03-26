class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # 尝试双指针
        s = 0
        f = 0
        for i in range(len(nums)):
            if nums[f]!=0:
                f+=1
                s+=1
            else:
                del nums[f]
                nums.append(0)
                
        return nums
                
                    