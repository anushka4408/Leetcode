class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=n
        squares=[]#1,4,9,
        i=1
        while i*i<=n:
            squares.append(i*i)
            i+=1
        x=len(squares)
        dp=[[-1 for i in range(sum+1)] for j in range(len(squares)+1)]
        def unbounded(x,sum):
            if(sum==0):
                return 0
            if(x==0 and sum>0):
                return float('inf')
            if(dp[x][sum]!=-1):
                return dp[x][sum]
            nottake=unbounded(x-1,sum)
            if(squares[x-1]<=sum):
                take=1+unbounded(x,sum-squares[x-1])
                dp[x][sum]=min(take,nottake)
            else:
                dp[x][sum]=nottake
            return dp[x][sum]
        return unbounded(x,sum)

        
        