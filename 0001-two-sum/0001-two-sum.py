class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, p in enumerate(nums):
            p2 = target - p
            if p2 in nums[index1+1:]:
                return [nums[:index1+1].index(p), index1+nums[index1+1:].index(p2)+1]