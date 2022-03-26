# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        while 1<=r:
            mid = (l+r)//2
            rst = guess(mid)
            if rst == 0:
                return mid
            elif rst == 1: #search right now
                l = mid+1
            else: r = mid-1
        