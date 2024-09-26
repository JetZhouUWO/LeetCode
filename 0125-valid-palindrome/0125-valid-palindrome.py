class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [c.lower() for c in s if c.isalnum()]
        if new_s == new_s[::-1]:
            return True
        return False