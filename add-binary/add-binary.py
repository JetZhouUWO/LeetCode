class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        total = str(int(a) + int(b))
        add_on = 0
        rst = ""
        # print(total)
        for i in range(len(total)-1,-1,-1):
            # print("i is ",i)
            # print("first add_on is ",add_on)
            num = str((int(total[i]) + add_on)%2)
            # print(num)
            add_on = (int(total[i]) + add_on)//2
            # print("finish add_on is", add_on)
            rst = "".join([num,rst])
            # print("update rst",rst)
            if ((i == 0) and (add_on == 1)):
                rst = "".join([str(add_on),rst])
        return rst