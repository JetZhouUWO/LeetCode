class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(","]":"[","}":"{"}
        stack = []
        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack