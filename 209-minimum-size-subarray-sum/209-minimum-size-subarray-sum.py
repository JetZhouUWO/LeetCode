class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        还是采用双指针算法, 左右一起开工
        """
        # i,j = 0,1
        # count = []
        # if sum(nums) < target:
        #     return 0
        # elif target in nums:
        #     return 1
        # else:
        #     while i<len(nums):
        #         if sum(nums[i:i+j]) < target:
        #             j+=1
        #         else:
        #             count.append(j+1)
        #             j = 0
        #             i+=1
        # return min(count)
    
    
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= target:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0