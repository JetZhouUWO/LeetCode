class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if needle == "":
        #     return 0
        # elif (needle in haystack):
        #         return haystack.index(needle)
        # else: return -1
        if needle == "":
             return 0
        else: return haystack.find(needle)
        