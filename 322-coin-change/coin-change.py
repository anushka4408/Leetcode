class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        dp=[[-1 for i in range(amount+1) ]for j in range(n+1)]
        def mincoins(coins,n,amount,s):
            if s==amount:
                return 0
            if n==0:
                return float('inf')
            if(dp[n][s]!=-1):
                return dp[n][s]
            if(s+coins[n-1]<=amount):
                take=1+mincoins(coins,n,amount,s+coins[n-1])
                notake=mincoins(coins,n-1,amount,s)
                dp[n][s]= min(take,notake)
            else:
                dp[n][s]=mincoins(coins,n-1,amount,s)
            return dp[n][s]

        ans= mincoins(coins,n,amount,0) 
        if(ans==float('inf')):
            return -1
        return ans

