class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # walk up #stops at A[i] >= A[i+1]
        N = len(arr)
        i = 0
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down #starts to walk down if A[i] > A[i+1]
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1

        return i == N-1
        
        