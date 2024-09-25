class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for idx, num in enumerate(nums):
            res += idx - num
        return res + len(nums)