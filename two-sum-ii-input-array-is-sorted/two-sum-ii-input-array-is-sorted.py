class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        #因为是sorted array, 尝试使用双指针, 左右尾部相加, 然后左右指针移动
        """
        i = 0 #左指针
        j = len(numbers) - 1 #右指针
        # for i in range(len(numbers)):
        #     test = target - numbers[i]
        #     if test in numbers[i+1:]:
        #         return [i+1,numbers[i+1:].index(test)+i+2]
        #         break
        while i<j:
            if (numbers[i] + numbers[j]) < target:
                i+=1
            elif (numbers[i] + numbers[j]) > target:
                j-=1
            else: return [i+1,j+1]
        