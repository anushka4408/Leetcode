class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

    # Step 1: Sort nums1
        sorted_nums1 = sorted(nums1)

    # Step 2: Calculate initial sum of differences
        initial_sum = 0
        max_reduction = 0

        for i in range(len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            initial_sum += diff

        # Step 3: Use binary search to find the closest value
            idx = bisect.bisect_left(sorted_nums1, nums2[i])

        # Check the closest element on the left
            if idx > 0:
                left_diff = abs(sorted_nums1[idx - 1] - nums2[i])
                max_reduction = max(max_reduction, diff - left_diff)

        # Check the closest element on the right
            if idx < len(sorted_nums1):
                right_diff = abs(sorted_nums1[idx] - nums2[i])
                max_reduction = max(max_reduction, diff - right_diff)

    # Step 4: Calculate the minimized sum
        minimized_sum = initial_sum - max_reduction
        return minimized_sum % MOD



    #     if nums1 == nums2:
    #         return 0

    # # Step 1: Calculate initial differences
    #     diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
    #     max_diff_index = diff.index(max(diff))

    # # Step 2: Find the best replacement
    #     min_diff = float('inf')
    #     best_replacement_index = -1
    #     for i in range(len(nums1)):
    #         if i != max_diff_index:  # Skip the same index
    #             new_diff = abs(nums1[i] - nums2[max_diff_index])
    #             if new_diff < diff[max_diff_index] and new_diff < min_diff:
    #                 min_diff = new_diff
    #                 best_replacement_index = i

    # # Step 3: Update the difference list
    #     if best_replacement_index != -1:
    #         diff[max_diff_index] = abs(nums1[best_replacement_index] - nums2[max_diff_index])

    # # Step 4: Return the sum of the differences
    #     return sum(diff) % (10**9 + 7)








        