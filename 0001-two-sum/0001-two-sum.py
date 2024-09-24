class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this one is my own thoughts
        # for index1, p in enumerate(nums):
        #     p2 = target - p
        #     if p2 in nums[index1+1:]:
        #         return [nums[:index1+1].index(p), index1+nums[index1+1:].index(p2)+1]

        # this one uses hash-map
        mapping = {}
        for idx, num in enumerate(nums):
            x = target - num
            if x in mapping:
                return [idx, mapping[x]]
            else:
                mapping[num] = idx