class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[-1]*(n)
        def robber(n):
            if(n<0):
                return 0
            if(dp[n]!=-1):
                return dp[n]
            take=nums[n]+robber(n-2)
            nottake=robber(n-1)
            dp[n]=max(take,nottake)
            return dp[n]
        return robber(n-1)

