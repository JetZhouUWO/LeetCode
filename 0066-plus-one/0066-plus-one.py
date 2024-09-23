class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # l = len(digits)
        # k = 0
        # for index, num in enumerate(digits):
        #     k+= num*(10**(l-1-index))
        # k+=1
        # k = str(k)
        # return [int(char) for char in k]

        l = len(digits)
        if digits[-1] + 1 != 10:
            digits[-1] = digits[-1] + 1
            return digits
        for i in range(l-1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] = digits[i]+1
                break
        
        if digits[0] == 0:
            return [1] + digits
        else:
            return digits