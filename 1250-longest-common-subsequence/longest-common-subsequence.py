class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n=len(text1)
        m=len(text2)
        dp=[[-1 for i in range(m+1)] for j in range(n+1)]

        def lcs(text1,text2,n,m):
            if(n==0 or m==0):
                return 0
            if(dp[n][m]!=-1):
                return dp[n][m]
            if(text1[n-1]==text2[m-1]):
                dp[n][m]=1+lcs(text1,text2,n-1,m-1)
            else:
                dp[n][m]=max(lcs(text1,text2,n-1,m),lcs(text1,text2,n,m-1))
            return dp[n][m]

        return lcs(text1,text2,n,m)