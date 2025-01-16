class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        uni=len(list(set(nums)))
        if n==uni:
            return False
        else: return True
