class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        print(nums)
        new=set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if(i not in new):
                res.append(i)
        return res
        