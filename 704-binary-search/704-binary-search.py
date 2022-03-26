class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 基本判断
        l,r = 0,len(nums)-1
        while l<=r: 
  
            mid = l + (r-l)//2 # (l+r)//2 也可以
  
        # 元素整好的中间位置
            if nums[mid] == target: 
                return mid 
          
        # 元素小于中间位置的元素，只需要再比较左边的元素
            elif nums[mid] > target: 
                r = mid-1 #mid-1 
  
        # 元素大于中间位置的元素，只需要再比较右边的元素
            else: 
                l = mid+1 #mid+1

        return -1
        