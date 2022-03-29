class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for item in range(1,num+1):
            if sum(int(ch) for ch in str(item)) % 2 == 0:
                count+=1
        return count
        