class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqie=set(nums)
        for i in uniqie:
            if(nums.count(i)>len(nums)//2):
                return i
        return -1
        