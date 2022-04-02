class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         def checkPalindrome(s,i,j):
#             while i<j:
#                 if s[i]!=s[j]:
#                     return False
#                 else:
#                     i+=1
#                     j-=1
#             return True
        
#         i = 0
#         j = len(s) -1
#         while i<j:
#             if s[i]!=s[j]:
#                 return checkPalindrome(s,i,j-1) or checkPalindrome(s,i+1,j)
#             i+=1
#             j-=1
#         return True
    
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                # one是del右边一个数字
                # two是del左边一个数字
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True
        