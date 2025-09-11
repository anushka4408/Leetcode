class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        s2=s[::-1]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if(s[i-1]==s2[j-1]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[n][n]




# class Solution(object):
#     def longestCommonSubsequence(self, text1, text2):
#         """
#         :type text1: str
#         :type text2: str
#         :rtype: int
#         """
#         n=len(text1)
#         m=len(text2)

#         dp=[[-1 for i in range(m+1)] for j in range(n+1)]
#         for i in range(1,n+1):
#             for j in range(1,m+1):
#                 if text1[i-1]==text2[j-1]:
#                     dp[i][j]=1+dp[i-1][j-1]
#                 else:
#                     dp[i][j]=max(dp[i-1][j],dp[i][j-1])
#         return dp[n][m]




#         # dp=[[0 for i in range(n+1)] for j in range(n+1)]
#         # s2="".join(s[::-1])
#         # # print(s2)
#         # for i in range(1,n+1):
#         #     for j in range(1,n+1):
#         #         if(s[i-1]==s2[j-1]):
#         #             dp[i][j]=1+dp[i-1][j-1]
#         #         else:
#         #             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
#         # return dp[n][n]
