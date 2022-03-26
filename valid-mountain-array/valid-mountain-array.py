class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
#         #单指针
#         # walk up #stops at A[i] >= A[i+1]
#         N = len(arr)
#         i = 0
#         while i+1 < N and arr[i] < arr[i+1]:
#             i += 1

#         # peak can't be first or last
#         if i == 0 or i == N-1:
#             return False

#         # walk down #starts to walk down if A[i] > A[i+1]
#         while i+1 < N and arr[i] > arr[i+1]:
#             i += 1

#         return i == N-1
    
        #双指针
        l = 0
        r = len(arr)-1
        
        #左边走到停止
        if len(arr) <3:
            return False
        while (l+1 < (len(arr)-1)) and (arr[l] < arr[l+1]):
            l+=1
        while (r-1 > 0) and (arr[r] < arr[r-1]):
            r-=1
        # if (l == 0) or (r == len(arr)-1):
        #     return False
        return l==r
        
        