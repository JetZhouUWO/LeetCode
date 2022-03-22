class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        这一版答案太慢
        """
        if len(nums) <= 1:
            return 0
        num_copy= list(set(nums))
        max_val = sorted(num_copy)[-1]
        num_copy.remove(max_val)
        second = sorted(num_copy)[-1]
        if max_val >= second*2:
            return nums.index(max_val)
        else:
            return -1
