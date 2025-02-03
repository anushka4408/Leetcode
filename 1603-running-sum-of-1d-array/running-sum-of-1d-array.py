class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        j=1
        for i in range(1,len(nums)):
            nums[i]=nums[j-1]+nums[i]
            j+=1
        return nums