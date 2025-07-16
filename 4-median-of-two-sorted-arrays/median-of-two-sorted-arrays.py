class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # If there are no elements left on the left side after partition
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            # If there are no elements left on the right side after partition
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if we have partitioned the arrays correctly
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If the total number of elements is even
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                # Move towards the left in nums1
                high = partitionX - 1
            else:
                # Move towards the right in nums1
                low = partitionX + 1

        raise ValueError("Input arrays are not sorted properly.")
