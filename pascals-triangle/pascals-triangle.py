class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rst = [None] * numRows
        arr_1 = [1]
        arr_2 = [1,1]
        #1行的情况:
        if numRows == 1:
            rst[0] = arr_1
            return rst
        #2行的情况:
        if numRows == 2:
            rst[0] = arr_1
            rst[1] = arr_2
            return rst
        #如果>2行
        rst[0] = arr_1
        rst[1] = arr_2
        for i in range(2,numRows,1):
            arr = [None] * (i+1)
            arr[0] = 1
            arr[i] = 1
            for j in range(1,i,1):
                arr[j] = rst[i-1][j-1] + rst[i-1][j]
            rst[i] = arr
        return rst