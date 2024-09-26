class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {}
        for idx, i in enumerate(nums):
            x = target - i
            if x in visit.keys():
                return [idx, visit[x]]
            visit[i] = idx