class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if(nums):
            n=len(nums)
            i=0
            while i<n:
                if(nums[i]==val):
                    nums[i]=nums[n-1]
                    n-=1
                else:
                    i+=1
            return n
        return 