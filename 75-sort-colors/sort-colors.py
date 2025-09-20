from collections import defaultdict
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # SELECTION SORT
        # for i in range(len(nums)):
        #     minidx=i
        #     for j in range(i+1,len(nums)):
        #         if(nums[j]<nums[minidx]):
        #             minidx=j
        #     nums[minidx],nums[i]=nums[i],nums[minidx]
        # return nums

        # BUBBLE SORT
        # for i in range(len(nums)):
        #     for j in range(0,len(nums)-i-1):
        #         if(nums[j]>nums[j+1]):
        #             nums[j],nums[j+1]=nums[j+1],nums[j]       
        # return nums
# Bubble sort is stable (doesn’t change order of equal elements).

# Time Complexity: O(n²)

# Space Complexity: O(1) (in-place sorting)

    # INSERTION SORT
        for i in range(1,len(nums)):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums


            
                