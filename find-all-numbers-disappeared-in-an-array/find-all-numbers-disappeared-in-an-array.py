class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        full_arr = [i for i in range(1,len(nums)+1)]
        return sorted(list(set(full_arr) - set(nums)))
        