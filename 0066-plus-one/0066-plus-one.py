class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] + 1 != 10:
            digits[-1]+= 1
            return digits
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] +1 != 10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits