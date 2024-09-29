class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {}
        for idx, num in enumerate(nums):
            if target - num in visit.keys():
                return [idx, visit[target-num]]
            visit[num] = idx
        return -1