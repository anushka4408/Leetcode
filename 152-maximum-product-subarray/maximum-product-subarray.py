class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans=maxproduct=minproduct=nums[0]
        for i in range(1,len(nums)):
            if(nums[i]<0):
                maxproduct,minproduct=minproduct,maxproduct
            maxproduct=max(maxproduct*nums[i],nums[i])
            minproduct=min(minproduct*nums[i],nums[i])
            ans=max(ans,maxproduct)
        return ans
        