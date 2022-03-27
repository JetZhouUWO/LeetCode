class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            if (arr[i] == 0):
                if 0 in arr[i+1:]:
                    return True
                    break
                else:
                    pass
            elif arr[i]%2 == 0:
                if ((2*arr[i] in arr) | (arr[i]//2 in arr)):
                    return True
                    break
            else:
                if (2*arr[i] in arr):
                    return True
                    break
        return False
        