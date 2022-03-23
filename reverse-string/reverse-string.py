class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0;
        j = len(s) - 1;
        while (i < j):
            s[j], s[i] = s[i], s[j]
            i+=1
            j-=1
        return s
        