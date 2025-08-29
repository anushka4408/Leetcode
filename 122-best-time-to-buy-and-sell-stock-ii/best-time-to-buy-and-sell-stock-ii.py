class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        # """
        n=len(prices)
        dp=[[-1]*2 for i in range(n)]
        def f(i,canBuy):
            if i==n:
                return 0
            if dp[i][canBuy]!=-1:
                return dp[i][canBuy]
            if canBuy==True:
                dp[i][canBuy]=max(-prices[i]+f(i+1,False),f(i+1,True))
            else:
                dp[i][canBuy]=max(prices[i]+f(i+1,True),f(i+1,False))
    
            return dp[i][canBuy] 
        return f(0,True)#f(i==0 , canBuy=True)









        profit=0
        for j in range(len(prices)-1):
            if(prices[j]<prices[j+1]):
                profit+=prices[j+1]-prices[j]
        return profit

        