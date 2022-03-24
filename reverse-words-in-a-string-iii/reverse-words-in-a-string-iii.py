class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        rst = [x[::-1] for x in l]
        return " ".join(rst)
        