class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        l,total,r=0,0,1
        while l+r < len(nums):
            if nums[l] != nums[l+r]:
                #print("r即将归零 ",r)
                total+=r*(r-1)//2
                #print('total 是', total)
                #print("l 是 ", l)
                l = l+r
                #print("l更新后是 ", l)
                r = 1
            else:
                r+=1
                #print("r继续",r)
        total+=r*(r-1)//2
        return total