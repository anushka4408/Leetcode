class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to use the two-pointer technique
        res = []
        n = len(nums)

        for i in range(n):
        # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[left] + nums[right]
            
                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                
                # Move pointers and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return res


        # nums.sort()
        # # -1+1+0=0,,-1+1=0,-1-1+2=0,,-1-1=-2
        # # i=0
        # # while i<=len(nums):
        # #     for j in range(i+1,)
        # k=-1
        # res=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         # print(-(nums[i]+nums[j]))
        #         if(-(nums[i]+nums[j]) in nums):
        #             k=nums.index(-(nums[i]+nums[j]))
        #             # print(i,j,k)
        #             if(i!=j and i!=k and j!=k):
        #                 res.append([nums[i],nums[j],nums[k]])
        #             else:
        #                 continue
        # return res

