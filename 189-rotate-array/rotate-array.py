class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     element=nums.pop()
        #     nums.insert(0,element)
        # return nums

        




        # for i in range(k):
        # #    element=nums.pop()
        # #    nums.insert(0,element)
        # nums.insert(0,nums.pop())
        # return nums

        # def reverse(nums,start,end):
        #     # reverse by swapping the start and end position
        #     while start<end:
        #         nums[start],nums[end]=nums[end],nums[start]
        #         # nums[start]=temp
        #         # nums[start]=nums[end]
        #         # nums[end]=temp
        #         start+=1
        #         end-=1
        #     return nums

        # k%=len(nums)
        # # first reverse the whole list =[7,6,5,4,3,2,1]
        # nums=reverse(nums,0,len(nums)-1)

        # # reverse first k elements=[5,6,7,4,3,2,1]
        # nums=reverse(nums,0,k-1)

        # #reverse last elements=[5,6,7,,,1,2,3,4]
        # nums=reverse(nums,k,len(nums)-1)
        

        k =k % len(nums)
        r= len(nums)-k
        new = nums[0:r] #[1,2,3,4]
        nums[0:r] =[] #[5,6,7]
        nums.extend(new) #[5,6,7,1,2,3,4]
        
        
