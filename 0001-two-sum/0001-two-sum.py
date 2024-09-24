class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this one is my own thoughts
        # for index1, p in enumerate(nums):
        #     p2 = target - p
        #     if p2 in nums[index1+1:]:
        #         return [nums[:index1+1].index(p), index1+nums[index1+1:].index(p2)+1]

        # this one uses hash-map
        mapping = {}
        for idx, i in enumerate(nums):
            x = target - i
            if x in mapping:
                return [idx, mapping[x]]
            mapping[i] = idx