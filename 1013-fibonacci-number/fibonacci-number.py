class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*(n+1)
        def fibb(n):
            if(n==0):
                return 0
            if(n==1):
                return 1
            if(dp[n]!=-1):
                return dp[n]
            dp[n]= fibb(n-1)+fibb(n-2)
            return dp[n]
        return fibb(n)

        
