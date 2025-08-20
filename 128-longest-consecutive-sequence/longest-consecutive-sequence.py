class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest=0
        newnums=set(nums)
        for num in newnums:
            if num-1 not in newnums:
                current=num
                length=1
                while current+1 in newnums:
                    current+=1
                    length+=1
                longest=max(length,longest)
        return longest