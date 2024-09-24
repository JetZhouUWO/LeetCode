class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        return False
    # can also use Counter() to compute the frequencies of each appeared letter
        