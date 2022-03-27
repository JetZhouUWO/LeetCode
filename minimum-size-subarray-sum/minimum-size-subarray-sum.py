class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        还是采用双指针算法, 左右一起开工
        """
        # count最开始用超过长度的数字,
        # 一旦全部加起来都达不到target, count就不会被更新, 最后可以返回0值
        left,total,count = 0,0,len(nums) + 1
        for right,n in enumerate(nums):
            #每次往后加一个数
            total += n
            #判断有没有大于等于target
            while total >= target:
                #更新count
                count = min(count,right-left+1)
                # 减掉最左边的值就是从左边的下一个值开始计算到当前值然后继续向后加
                # 这样可以避免每次都重新算一遍到当前位子的sum
                total-=nums[left]
                # 左指针推进一步
                left +=1
        return count if count<=len(nums) else 0
    
    
        # total = left = 0
        # result = len(nums) + 1
        # for right, n in enumerate(nums):
        #     total += n
        #     while total >= target:
        #         result = min(result, right - left + 1)
        #         total -= nums[left]
        #         left += 1
        # return result if result <= len(nums) else 0