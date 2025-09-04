class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n=len(str1)
        m=len(str2)
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(str1[i-1]==str2[j-1]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        lcs=dp[i][j]
        print(n+m-lcs)
        ans=[]
        i=n
        j=m
        while i>0 and j>0:
            if(str1[i-1]==str2[j-1]):
                ans.append(str1[i-1])
                i-=1
                j-=1
            else:
                if(dp[i-1][j]>dp[i][j-1]):
                    ans.append(str1[i-1])
                    i-=1
                else:
                    ans.append(str2[j-1])
                    j-=1
        while i>0:
            ans.append(str1[i-1])
            i-=1
        while j>0:
            ans.append(str2[j-1])
            j-=1

        ans.reverse()
        return "".join(ans)

