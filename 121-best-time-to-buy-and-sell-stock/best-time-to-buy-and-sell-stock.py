class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #1.
        # profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if(prices[j]>prices[i]):
        #             profit=max(profit,prices[j]-prices[i])
        #         else:
        #             j+=1
        # return profit

        #2.
        # i=0
        # profit=0
        # for j in range(1,len(prices)):
        #     if prices[i]<prices[j]:
        #         curr=prices[j]-prices[i]
        #         profit=max(profit,curr)
        #     else:
        #         i=j
        # return profit

        #3.Using recursion
        #4.Using Memoization
        #5.Using Tabulation
        min_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return profit

            

        