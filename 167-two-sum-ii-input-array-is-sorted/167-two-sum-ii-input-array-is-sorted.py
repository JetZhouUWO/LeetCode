class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0 #左指针
        j = len(numbers) - 1 #右指针

        while i<j:
            if (numbers[i] + numbers[j]) == target:
                return [i+1,j+1]
            elif (numbers[i] + numbers[j]) > target:
                j-=1
            else: i+=1
        return [-1,-1]