class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = list(set(nums))
        a.sort()
        if len(a) <3:
            return a[-1]
        else:
            return a[-3]
        