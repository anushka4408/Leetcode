class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Place each number in its correct position: nums[i] = i + 1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # Find the first location where the index doesn't match the value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positions are filled correctly, the missing number is n + 1
        return n + 1
