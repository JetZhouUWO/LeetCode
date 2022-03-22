class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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
        