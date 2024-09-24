class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {"]":"[","}":"{",")":"("}
        for char in s:
            if char in mappings.values():
                stack.append(char)
            elif char in mappings.keys():
                if not stack or mappings[char]!= stack.pop():
                    return False
        return not stack