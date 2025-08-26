class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #1.
        for i in range(len(nums)):
            diff=target-nums[i]
            if(diff in nums and nums.index(diff)!=i):
                return i,nums.index(diff)