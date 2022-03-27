class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        #如果是empty matrix, return 空的arr
        if not mat or not mat[0]:
            return []
        
        #查看matrix的size
        N,M = len(mat), len(mat[0]) #len(mat)是行, len(mat[0])是多少列
        
        # 一共有N+M-1的arr要算, 有些会reverse, 有些不用
        # 创建一个rst arr和中间用来算每个单独arr的arr
        rst, intermediate = [],[]
        for x in range(N+M-1):
            #每次清空Intermediate
            intermediate = []
            r = 0 if x < M else x-M +1
            c = x if x < M else M-1
            while r < N and c>-1:
                intermediate.append(mat[r][c])
                r+=1
                c-=1
            if x%2 == 0:
                rst.extend(intermediate[::-1])
            else:
                rst.extend(intermediate)
                
        return rst
        