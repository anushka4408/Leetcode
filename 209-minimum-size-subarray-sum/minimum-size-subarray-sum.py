class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minlength=float('inf')
        left=0
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                minlength=min(minlength,i-left+1)
                total-=nums[left]
                left+=1
        return 0 if minlength==float('inf') else minlength





        