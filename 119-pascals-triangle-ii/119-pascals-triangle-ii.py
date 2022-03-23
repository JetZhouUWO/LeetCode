class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #基本情况, 2行
        res = [[1],[1,1]]
        #如果只有一行
        if rowIndex ==0:
            return res[0]
        #如果只有两行
        elif rowIndex==1:
            return res[1]
        #如果多于两行
        else:
            for level in range(2,rowIndex+1):
                tmp_response=[1]
                
                for i in range(level-1):
                    # 直接用res里当时里面最后一个arr来做
                    # 第2行就应该有一个数字, 第三行两个中间数字, etc
                    # tmp_value = res[-1][i] + res[-1][i+1]
                    tmp_response.append(res[-1][i] + res[-1][i+1])
                #加最后一个1
                tmp_response.append(1)
                res.append(tmp_response)
            return tmp_response
        