class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # total = []
        # for i in range(len(accounts)):
        #     total.append(sum(accounts[i]))
        # return max(total)
        
        for i in range(len(accounts)):
            accounts[i] = sum(accounts[i])
        return max(accounts)
        