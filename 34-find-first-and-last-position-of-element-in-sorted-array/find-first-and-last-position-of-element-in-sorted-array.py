class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n)=time complexity
        # start=-1
        # end=-1
        # for i in range(len(nums)):
        #     if(nums[i]==target):
        #         start=i
        #         break
        # for i in range(len(nums)-1,-1,-1):
        #     if(nums[i]==target):
        #         end=i
        #         break
        # return [start,end]

        # For O(logn) use Binary search on start and end
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        start = findFirst(nums, target)
        end = findLast(nums, target)

    # Check if the target exists in the list
        if start <= end and start < len(nums) and nums[start] == target:
            return [start, end]
        return [-1, -1]
                