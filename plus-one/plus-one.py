class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        for i in range(len(digits)):
            num += str(digits[i])
        num = int(num) + 1
        return [int(x) for x in str(num)]
        
        