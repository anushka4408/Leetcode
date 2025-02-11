class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()  # To track unique elements
        write_index = 0  # Tracks position to overwrite in nums

        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[write_index] = num  # Place the unique number at the current index
                write_index += 1

        # nums is now modified in-place to contain only unique elements
        return write_index  # Length of the modified list of unique elements
