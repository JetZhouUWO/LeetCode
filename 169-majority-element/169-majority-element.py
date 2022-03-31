class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {x: nums.count(x) for x in list(set(nums))}
        return max(d, key=d.get)
        