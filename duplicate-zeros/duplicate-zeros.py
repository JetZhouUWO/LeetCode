class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        j = 0
        N = len(arr)
        while j < N:
            if arr[j]!=0:
                j+=1
            else:
                arr.insert(j,0)
                del arr[-1]
                j+=2
                #N+=1
        return arr
        