class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #尝试使用双指针
        count = 1
        j = 0
        # if len(nums) == 1:
        #     return count
        # if len(nums) == len(set(nums)):
        #     return len(nums)
        N = len(nums) -1
        while j < len(nums)-1:
            if nums[j] == nums[j+1]:
                del nums[j+1]
                # update一下长度
                N = len(nums) -1
            elif nums[j] != nums[j+1]:
                j+=1
                count +=1
            elif nums[j] == -1000:
                count-=1
                return count
        