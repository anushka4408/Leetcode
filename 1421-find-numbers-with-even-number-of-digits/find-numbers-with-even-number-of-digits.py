class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def countdigits(i):
            count=0
            if(i==0):
                return 1
            while i!=0: 
                i= i//10
                count+=1
            return count 
        even=0
        for num in nums:
            if(countdigits(num)%2==0):
                even+=1
        return even