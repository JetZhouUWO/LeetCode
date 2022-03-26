class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] < nums[mid+1]:
                l = mid +1
                
            #不用mid+1因为如果mid比右边数字大, mid有可能就是最大值, 不能除开一个大值
            else: r = mid
        return l
        