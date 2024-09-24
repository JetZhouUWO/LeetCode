class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_1 = [char.lower() for char in s if char.isalnum()]
        if s_1 == s_1[::-1]:
            return True
        return False