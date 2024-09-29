class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] + 1 != 10:
            digits[-1] += 1
            return digits
        
        for l in range(len(digits)-1,-1,-1):
            if digits[l] + 1 != 10:
                digits[l] += 1
                return digits
            else:
                digits[l] = 0
            
        return [1] + digits