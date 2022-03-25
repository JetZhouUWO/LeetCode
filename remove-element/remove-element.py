class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #尝试使用双指针
        i,j,count = 0,len(nums)-1,0
        while i<=j:
            if nums[i]!= val:
                i+=1
            elif ((nums[i] == val) & (nums[j]!=val)):
                nums[i],nums[j] = nums[j],nums[i]
                j-=1
                count+=1
                i+=1
                del nums[-1]
            elif ((nums[i] == val) & (nums[j]==val)):
                j-=1
                del nums[-1]
        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k += 1
        # return k
        
        # while(val in nums):
        #     nums.remove(val)
        
        