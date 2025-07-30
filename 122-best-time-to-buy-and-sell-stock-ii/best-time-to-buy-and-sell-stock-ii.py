class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        for j in range(len(prices)-1):
            if(prices[j]<prices[j+1]):
                profit+=prices[j+1]-prices[j]
        return profit

        