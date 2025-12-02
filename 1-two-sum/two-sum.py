class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if(diff in seen):
                return [i,nums.index(diff)]
            seen[nums[i]]=diff
        