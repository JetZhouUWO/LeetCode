class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        hint: We can precompute prefix sums P[i] = nums[0] + nums[1] + ... + nums[i-1]. 
        Then for each index, the left sum is P[i], and the right sum is P[P.length - 1] - P[i] - nums[i].
        """
        #num的总和
        S = sum(nums)
        #从左算起0
        leftsum = 0
        for i, x in enumerate(nums): # i = 0,1,2,3, x=对应index的数字
            #测试如果left sum = 总和 - 左边和 - 中间数字 = 右边和
            if leftsum == (S - leftsum - x):
                #return这个index
                return i
            #继续加左边
            leftsum +=x
        #如果加到最后都没有就return -1
        return -1
        