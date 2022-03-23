class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        l.reverse()                #to reverse in place instead of a copy via l[::-1]
        return " ".join(l)
        