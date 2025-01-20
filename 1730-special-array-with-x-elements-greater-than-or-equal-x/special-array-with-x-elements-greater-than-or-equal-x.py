class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  # Sort in descending order
        for i in range(len(nums)):
            if i + 1 <= nums[i]:  # Check if the current index + 1 matches the value
                if i == len(nums) - 1 or nums[i + 1] < i + 1:
                    return i + 1
        return -1

        



        # count=0
        # res=0
        # for i in range(len(nums)):
        #     if( nums[i]>min(nums)):
        #         count+=1
        # for i in range(len(nums)):
        #     if(nums[i]>=count):
        #         res+=1
        # if(res==count):
        #     return res
        # else:
        #     return -1