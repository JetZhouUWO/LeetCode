class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        k = 0
        for index, num in enumerate(digits):
            k+= num*(10**(l-1-index))
        k+=1
        k = str(k)
        return [int(char) for char in k]