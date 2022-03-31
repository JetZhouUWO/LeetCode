class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #自己写的
        # nums = sorted(nums)
        # if len(nums) == 1:
        #     return nums[0]
        # i = 0
        # while i <= len(nums)//2:
        #     if i == len(nums)//2:
        #         return nums[2*i]
        #     elif nums[2*i] == nums[2*i+1]:
        #         print("Passing number",nums[2*i])
        #         i+=1
        #     else:
        #         return nums[2*i]
            
        return 2*sum(set(nums))-sum(nums)
        
        