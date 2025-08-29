class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum=nums[0]
        currentsum=nums[0]
        for i in range(1,len(nums)):
            currentsum=max(nums[i],nums[i]+currentsum)
            maxsum=max(currentsum,maxsum)
        return maxsum
            