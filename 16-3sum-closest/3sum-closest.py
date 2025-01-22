class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest=float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                currentsum=nums[i]+nums[left]+nums[right]
                if(abs(currentsum-target)<abs(closest-target)):
                    closest=currentsum
                if(currentsum>target):
                    right-=1
                elif(currentsum<target):
                    left+=1
                else:
                    return currentsum
        return closest






