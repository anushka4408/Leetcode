class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i=0
        profit=0
        for j in range(1,len(prices)):
            if prices[i]<prices[j]:
                curr=prices[j]-prices[i]
                profit=max(profit,curr)
            else:
                i=j
        return profit
            

        