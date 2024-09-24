class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if Counter(s) == Counter(t):
        #     return True
        # return False
        new_s = [char for char in s]
        new_t = [char for char in t]
        new_s.sort()
        new_t.sort()
        if new_s == new_t:
            return True
        return False
        