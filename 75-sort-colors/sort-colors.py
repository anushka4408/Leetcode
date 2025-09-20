from collections import defaultdict
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # SELECTION SORT
        # for i in range(len(nums)):
        #     miniind=i
        #     for j in range(i+1,len(nums)):
        #         if(nums[j]<nums[miniind]):
        #             miniind=j
        #     nums[i],nums[miniind]=nums[miniind],nums[i]
        # return nums

        # BUBBLE SORT
        # for i in range(len(nums)):
        #     for j in range(0,len(nums)-1-i):
        #         if(nums[j]>nums[j+1]):
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        # return nums

        # INSERTION SORT
        # for i in range(1,len(nums)):
        #     key=nums[i]
        #     j=i-1
        #     while j>=0 and nums[j]>key:
        #         nums[j+1]=nums[j]
        #         j-=1
        #     nums[j+1]=key
        # return nums
        return nums.sort()

            





        # for i in range(len(nums)):
        #     # swapped=False
        #     for j in range(len(nums)-i-1):
        #         if(nums[j]>nums[j+1]):
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        #             # swapped=True
        #     # if not swapped:
        #     #     break
                