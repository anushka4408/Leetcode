class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[0]*2*n 
        # this is used to set ans to 6 index with zero
        for i in range(n):
            ans[i]=nums[i]
            ans[i+n]=nums[i]

        return ans
            