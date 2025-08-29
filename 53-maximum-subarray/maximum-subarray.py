class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [-1] * n

        def f(i):
            if i == 0:
                return nums[0]
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(nums[i], nums[i] + f(i-1))
            return dp[i]

        ans = float('-inf')
        for i in range(n):
            ans = max(ans, f(i))
        return ans



        # maxsum=nums[0]
        # currentsum=nums[0]
        # for i in range(1,len(nums)):
        #     currentsum=max(nums[i],nums[i]+currentsum)
        #     maxsum=max(currentsum,maxsum)
        # return maxsum
            