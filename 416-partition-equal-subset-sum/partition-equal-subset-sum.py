class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Recursion
        # total=sum(nums)
        # if(total%2!=0):
        #     return False
        # target=total//2

        # def subset(n,s):
        #     if(s==target):
        #         return True
        #     if(n==0 or s>target):
        #         return False
        #     return ( subset(n-1,s+nums[n-1]) or subset(n-1,s))
        # return subset(len(nums),0)


        total=sum(nums)
        if(total%2!=0):
            return False
        target=total//2
        dp=[[-1]*(target+1) for i in range(len(nums)+1)]
        def subset(n,s):
            if(s==target):
                return True
            if(n==0 or s>target):
                return False
            if(dp[n][s]!=-1):
                return dp[n][s]
            take=subset(n-1,s+nums[n-1])
            nottake=subset(n-1,s)
            dp[n][s]=take or nottake
            return dp[n][s]
        return subset(len(nums),0)

            
        