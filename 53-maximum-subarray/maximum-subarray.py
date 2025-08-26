class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxSubArrayRec(nums, i, curr_sum):
            if i == len(nums):
                return float("-inf")   # no subarray
    
            # continue subarray or start fresh
            curr_sum = max(nums[i], curr_sum + nums[i])
    
            # best for this position vs later positions
            return max(curr_sum, maxSubArrayRec(nums, i+1, curr_sum))

        return maxSubArrayRec(nums, 0, 0)
