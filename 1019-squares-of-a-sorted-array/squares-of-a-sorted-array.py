class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     nums[i]=nums[i]**2
        # nums.sort()
        # return nums

        return sorted(map(lambda x:x**2,nums)) 
        # for i in range(len(nums)-1):
        #     newel=nums[i+1]
        #     j=i+1
        #     while j>0 and nums[j-1]>newel:
        #         nums[j]=nums[j-1]
        #         j-=1
        #     nums[j]=newel
        # return nums
