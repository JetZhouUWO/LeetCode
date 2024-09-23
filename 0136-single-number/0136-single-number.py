class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums):
            if i == (len(nums)-1):
                return nums[i]
                
            p1 = nums[i]
            p2 = nums[i+1]
            if p1 == p2:
                i+=2
            else:
                return nums[i]