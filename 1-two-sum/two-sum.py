class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            diff=target-nums[i]
            if(diff in nums and nums.index(diff)!= i):
                return i,nums.index(diff)











        # n=len(nums)
        # for i in range(n):
        #     diff=target-nums[i]
        #     for j in range(i+1,n):
        #         if nums[j]==diff:
        #             return [i,j]
        