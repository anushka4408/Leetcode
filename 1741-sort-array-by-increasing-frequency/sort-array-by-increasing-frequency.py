class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        new=set(nums)
        for i in new:
            freq[i]=nums.count(i)
        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
    
    # Step 2: Sort the numbers based on their frequency and value in decreasing order for ties
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
    
        return sorted_nums


