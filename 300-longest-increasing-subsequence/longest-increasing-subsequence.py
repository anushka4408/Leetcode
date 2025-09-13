class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[1]*(n+1)
        for i in range(n):
            for j in range(i):
                if(nums[i]>nums[j]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

            
        

        












        # n = len(nums)
        # dp = [1] * n   # LIS ending at each index is at least 1
        
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        
        # return max(dp)
            
