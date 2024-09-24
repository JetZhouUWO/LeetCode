class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for idx,i in enumerate(nums):
            res += idx - i
        return res + n