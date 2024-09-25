class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {}
        for idx,n in enumerate(nums):
            if target-n in visit.keys():
                return [idx, visit[target-n]]
            visit[n] = idx
        return -1