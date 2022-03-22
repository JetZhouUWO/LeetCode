class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        num = 0
        for i,x in enumerate(digits):
            num += x*(10**(n-1-i))
        num += 1
        b=len(str(num))
        new_digits = [None] * b
        for i in range(b):
            new_digits[i] = num // (10**(b-i-1))
            num = num % (10**(b-i-1))
        return new_digits
        
