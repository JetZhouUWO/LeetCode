class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num == 1:
        #     return  True
        # arr = [i for i in range(1,num)]
        l, r= 1,num
        while l<=r:
            mid = l + (r-l)//2
            if mid**2 == num:
                return True
            elif mid**2 < num:
                l = mid+1
            else: r = mid-1
        return False
            