class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # res = []
        # for i, j in zip(nums[:n],nums[n:]):
        #     res += [i,j]
        # return res
        rst = []
        for i in range(n):
            rst.append(nums[i])
            rst.append(nums[i+n])
        return rst