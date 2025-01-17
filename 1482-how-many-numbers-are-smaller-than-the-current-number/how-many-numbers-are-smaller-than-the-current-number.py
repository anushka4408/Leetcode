class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            smallest=0
            for j in range(len(nums)):
                if(nums[j]<nums[i] and j!=i):
                    smallest+=1
            res.append(smallest)
        return res

