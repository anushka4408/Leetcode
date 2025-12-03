class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        
        dp=[[-1 for i in range(amount+1)] for j in range(n+1)]
        def unbounded(n,amount):
            if(amount==0):
                return 0
            if(n==0 and amount>0):
                return float('inf')
            if(dp[n][amount]!=-1):
                return dp[n][amount]
            nottake=unbounded(n-1,amount)
            if(coins[n-1]<=amount):
                take=1+unbounded(n,amount-coins[n-1])
                dp[n][amount]=min(take,nottake)
            else:
                dp[n][amount]=nottake
            return dp[n][amount]
        ans= unbounded(n,amount)
        return -1 if ans==float('inf') else ans
            
            

