class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if(n==0):
            return nums1
            # print(nums1)
        elif(m==0):
            for i in range(len(nums1)):
                nums1[i]=nums2[i]
            # print(nums1)

            return nums1
        else:
            i=m
            while i<len(nums1):
                for j in range(n):
                    nums1[i]=nums2[j]
                    i+=1
        return nums1.sort()
        # print(nums1.sort())



        
