class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num=sum(nums)-sum(set(nums))
        summ=0
        for i in range(1,len(nums)+1):
            summ+=i
        return[num,summ-sum(set(nums))]


