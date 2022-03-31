class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #使用双指针识别
        l,r = 0,len(s)-1
        print(l,r)
        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else:
                if s[l].lower() == s[r].lower():
                    l+=1
                    r-=1
                else:
                    return False
        return True
        