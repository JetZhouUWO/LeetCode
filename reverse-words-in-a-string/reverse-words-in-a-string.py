class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        regex = r'\b\w+\b'
        list1=re.findall(regex,s)
        list1.reverse()
        return " ".join(list1)
        