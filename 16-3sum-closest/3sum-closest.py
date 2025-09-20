class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        closest=float('inf')
        for i in range(n-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            left=i+1
            right=n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if(abs(total-target)<closest):
                    closest=abs(total-target)
                    ans=total
                    # while left<right and nums[left]==nums[left+1]:
                    #     left+=1
                    # while left<right and nums[right]==nums[right-1]:
                    #     right-=1
                    # left+=1
                    # right-=1
                elif total<target:
                    left+=1
                elif total>target:
                    right-=1
                else:
                    return total
        return ans
                





