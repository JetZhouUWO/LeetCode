class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1 = ''.join(reversed(str(x)))
        return x1 == str(x)