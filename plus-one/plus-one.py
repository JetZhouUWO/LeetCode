class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        for i in range(len(digits)):
            num += str(digits[i])
        # num =  int(''.join(map(str, digits)))
        # num = int(''.join([str(dig) for dig in digits]))
        num = int(num) + 1
        return [int(x) for x in str(num)]
        
        
