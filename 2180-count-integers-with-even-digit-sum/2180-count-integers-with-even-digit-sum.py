class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for item in range(1,num+1):
            #print(item)
            #print(sum(int(ch) for ch in str(item)))
            if sum(int(ch) for ch in str(item)) % 2 == 0:
                count+=1
                #print(item)
        return count
        