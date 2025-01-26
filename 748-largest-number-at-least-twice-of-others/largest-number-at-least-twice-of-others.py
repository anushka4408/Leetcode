class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum=max(nums)
        print(nums)
        for i in nums:
            if(i*2>maxnum and i!=maxnum):
                return -1
        return nums.index(maxnum)