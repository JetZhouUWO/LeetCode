class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) == len(set(nums)):
            return False
        return True

        