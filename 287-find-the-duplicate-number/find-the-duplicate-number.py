class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=set()
        for i in range(len(nums)):
            if(nums[i] not in num):
                num.add(nums[i])
            else:
                return nums[i]
                
    
                
