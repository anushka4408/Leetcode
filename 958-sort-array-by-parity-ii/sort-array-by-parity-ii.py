class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_idx = 0
        odd_idx = 1
        n = len(nums)
        res = [0] * n

        for num in nums:
            if num % 2 == 0:
                res[even_idx] = num
                even_idx += 2
            else:
                res[odd_idx] = num
                odd_idx += 2

        return res